import re
import json
import numpy as np
import pandas as pd

goods = pd.read_csv('../data/Goods.csv', quotechar='"')
recipes = pd.read_csv('../data/Workshops_Recipes.csv', quotechar='"')

# Goods Data
filt = re.compile('(\s*\[.+?\]\s*)|(\s*Ruins\s*)|(\s*\(.+?\)\s*)|(\s*T[0-9]\s*)')
columns = list(goods.columns[1:-1])
goods_data = {}
for i, name in enumerate(goods.loc[:, 'id']):
    if not '_Meta' in name:
        good_name = filt.sub('', name).strip()
        goods_data[good_name] = {col: goods.loc[i, col] for col in columns}

# Recipe Data
columns = list(recipes.columns[1:-1])
recipe_data = {}
for i, name in enumerate(recipes.loc[:, 'id']):
    grade = name.split(' ')[-1]
    if grade[0] != 'T' or len(grade) != 2:
        grade = 'T3'
    good_name = filt.sub('', name).strip()
    
    if good_name == 'Tools Simple':
        good_name = 'Simple Tools'
    elif good_name == 'Workshop Eggs':
        good_name = 'Eggs'
    
    if good_name not in recipe_data:
        recipe_data[good_name] = {grade: {}}
    elif grade not in recipe_data[good_name]:
        recipe_data[good_name][grade] = {}
    ingredients = []
    cur_ingredient = -1
    for col in columns:
        val = recipes.loc[i, col] if pd.notna(recipes.loc[i, col]) else ''
        if col == 'product' or 'ingredient' in col:
            val = filt.sub(' ', val)
            if val:
                val = val.split(' ', maxsplit=1)
                val[0] = int(val[0])
            else:
                continue
            
            if 'ingredient' in col:
                n_ingr = int(col.replace('ingredient', '')[0]) -1
                if cur_ingredient != n_ingr:
                    cur_ingredient = n_ingr
                    ingredients.append([])
                ingredients[n_ingr].append(val)
        if 'ingredient' not in col:
            recipe_data[good_name][grade][col] = val
    
    recipe_data[good_name][grade]['ingredients'] = ingredients

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
