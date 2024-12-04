import requests
import pandas as pd
from tqdm import tqdm

do_for = 'Goods'  # Perks or Goods
df = pd.read_csv(f'../data/{do_for}.csv')

base = 'https://hoodedhorse.com/wiki/Against_the_Storm/Special:FilePath/'
for name in tqdm(df.loc[:, 'iconName']):
    img_data = requests.get(f'{base}{name}.png').content
    with open(f'../img/{do_for.lower()}/{name}.png', 'wb') as file:
        file.write(img_data)
