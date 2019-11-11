from numpy.random import choice
from collections import Counter

total_count = 100000

items = ['a', 'b', 'c', 'd', 'e']
probability = [0.4, 0.3, 0.2, 0.05, 0.05]
rand_items = choice(items, total_count, p=probability)
items_counter = Counter(rand_items)

for item, count in items_counter.most_common():
    print(f"{item}: {100 * count / total_count:.1f}%")