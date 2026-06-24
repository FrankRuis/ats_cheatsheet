import requests
import pandas as pd
from tqdm import tqdm

do_for = 'Goods'  # Perks or Goods
df = pd.read_csv(f'../data/{do_for}.csv')

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
}

cookies = {
    "cf_clearance": "yourCookie"
}
base = 'https://hoodedhorse.com/wiki/Against_the_Storm/Special:FilePath/'
for name in tqdm(df.loc[:, 'iconName']):
    img_data = requests.get(f'{base}{name}.png', headers=headers, cookies=cookies).content
    with open(f'../img/{do_for.lower()}/{name}.png', 'wb') as file:
        file.write(img_data)
