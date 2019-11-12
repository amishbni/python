from random_selection import select
from collections import Counter
from numpy.random import choice
from time import time

def test(array, total_count, probability, method):
    methods = {
        "numpy.random.choice": choice(array, total_count, p=probability),
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


def main():
    total_count = 1000000
    array = ['a', 'b', 'c', 'd']
    probability = [0.7, 0.1, 0.1, 0.1]

    print(f"array: {array}")
    print(f"probability: {probability}")
    print(f"size: {total_count}")

    print()

    print('random_selection.select: ')
    start_time = time()
    result = test(array, total_count, probability, 'random_selection.select')
    end_time = time()
    print(result)
    print(f"{(end_time - start_time):.4f} s")

    print()

    print('numpy.random.choice: ')
    start_time = time()
    result = test(array, total_count, probability, 'numpy.random.choice')
    end_time = time()
    print(result)
    print(f"{(end_time - start_time):.4f} s")


if __name__ == "__main__":
    main()
