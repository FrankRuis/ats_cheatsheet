import numpy as np

needs = {
    'Human': ['Porridge', 'Biscuits', 'Pie', 'Coats', 'Leisure', 'Religion'],
    'Beaver': ['Pickled Goods', 'Biscuits', 'Coats', 'Leisure', 'Education', 'Luxury'],
    'Harpy': ['Jerky', 'Education', 'Coats', 'Treatment', 'Boots', 'Paste'],
    'Lizard': ['Jerky', 'Pickled Goods', 'Pie', 'Skewers', 'Brawling', 'Boots'],
    'Fox': ['Porridge', 'Pickled Goods', 'Treatment', 'Skewers', 'Religion', 'Boots'],
    'Frog': ['Porridge', 'Pie', 'Brawling', 'Religion', 'Luxury', 'Boots', 'Paste']
}

overlapping_needs = {}
for s, ns in needs.items():
    for n in ns:
        if n not in overlapping_needs:
            overlapping_needs[n] = []
        overlapping_needs[n].append(s)

print(overlapping_needs)
