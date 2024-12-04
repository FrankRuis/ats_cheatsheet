import re
import json
import numpy as np
import pandas as pd

goods = pd.read_csv('../data/Goods.csv', quotechar='"')

# Goods Data
filt = re.compile(r'(\s*\[.+?\]\s*)|(\s*Ruins\s*)|(\s*\(.+?\)\s*)|(\s*T[0-9]\s*)')
columns = list(goods.columns[1:-1])
goods_data = {}
for i, name in enumerate(goods.loc[:, 'id']):
    if not '_Meta' in name:
        good_name = filt.sub('', name).strip()
        goods_data[good_name] = {col: goods.loc[i, col] for col in columns}
        goods_data[good_name]['description'] = goods_data[good_name]['description'].split('\r')[0].strip()

# Recipe Data
with open('../data/Workshops.json') as file:
    workshops = json.load(file)

recipe_data = {}
for workshop in workshops:
    for recipe in workshop['recipes']:
        good_name = recipe['product']['name'].split(']')[-1].strip()
        if good_name not in recipe_data:
            recipe_data[good_name] = {}
        
        grade = recipe['grade']
        grade_id = f'T{grade[-1]}'
        if grade_id not in recipe_data[good_name]:
            recipe_data[good_name][grade_id] = {}
        recipe_data[good_name][grade_id]['product'] = [recipe['product']['amount'], good_name]
        
        if 'ingredients' not in recipe_data[good_name][grade_id]:
            recipe_data[good_name][grade_id]['ingredients'] = []
        
        for ingredients in recipe['ingredients']:
            ings = []
            for ingredient in ingredients:
                ings.append([ingredient['amount'], ingredient['name'].split(']')[-1].strip()])
            recipe_data[good_name][grade_id]['ingredients'].append(ings)

# Ingredient Sets
good_ingredient_sets = {}
for good in recipe_data:
    for grade in recipe_data[good]:
        for ingredients in recipe_data[good][grade]['ingredients']:
            iset = []
            for ingredient in ingredients:
                if good not in good_ingredient_sets:
                    good_ingredient_sets[good] = []
                iset.append(ingredient[1])
            good_ingredient_sets[good].append(tuple(iset))
    good_ingredient_sets[good] = list(set(good_ingredient_sets[good]))

# Reverse ingredient sets
reverse_sets = {}
for good in good_ingredient_sets:
    for ingredient_set in good_ingredient_sets[good]:
        for ingredient in ingredient_set:
            if ingredient not in reverse_sets:
                reverse_sets[ingredient] = []
            reverse_sets[ingredient].append(good)

# Add Info
for good in goods_data:
    isets = good_ingredient_sets[good] if good in good_ingredient_sets else []
    goods_data[good]['ingredient_sets'] = isets
    goods_data[good]['reverse_set'] = [reverse_sets[good]] if good in reverse_sets else []
    goods_data[good]['icon_path'] = f'img/goods/{goods_data[good]["iconName"]}.png'

# Pandas using numpy types, which json does not like
class CustomJSONizer(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.bool_):
            val = super().encode(bool(obj))
        elif isinstance(obj, np.int64):
            val = super().encode(int(obj))
        else:
            val = super().default(obj)
        return val

text = '\'' + json.dumps(goods_data, cls=CustomJSONizer).replace("'", '\\\'') + '\''

with open('../js/goods.json', 'w') as file:
    file.write(f'goods_data = {text}')
