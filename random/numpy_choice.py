from numpy.random import choice
from collections import Counter

def select(array, total_count, probability):
    probability_dict = {}
    rand_items = choice(array, total_count, p=probability)
    items_counter = Counter(rand_items)

    for item, count in items_counter.most_common():
        probability_dict[item] = f"{100 * count / total_count:.1f}%"
    return probability_dict
