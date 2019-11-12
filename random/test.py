from random_selection import select
from collections import Counter

def test(array, total_count, probability):
    probability_dict = {}
    rand_items = select(array, total_count, probability)
    items_counter = Counter(rand_items)

    for item, count in items_counter.most_common():
        probability_dict[item] = f"{100 * count / total_count:.1f}%"
    return probability_dict


print(test(
    ['a', 'b', 'c', 'd'],
    1000000,
    [0.7, 0.1, 0.1, 0.1]
))