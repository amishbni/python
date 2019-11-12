from random_selection import select
from collections import Counter
from numpy.random import choice

def test(array, total_count, probability, method):
    methods = {
        "numpy.random.choice": choice(array, total_count, probability),
        "random_selection.select": select(array, total_count, probability)
    }

    if(method in methods):
        probability_dict = {}
        rand_items = methods[method]
        items_counter = Counter(rand_items)

        for item, count in items_counter.most_common():
            probability_dict[item] = f"{100 * count / total_count:.1f}%"
        return probability_dict
    else:
        raise ValueError(f"Method {method} has not been defined.")


print(test(
    ['a', 'b', 'c', 'd'],
    1000000,
    [0.7, 0.1, 0.1, 0.1],
    "random_selection.select"
))