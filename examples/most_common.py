import heapq
import re
import string

from collections import defaultdict, namedtuple
from typing import Iterable


def nlargest(n: int, iterable: Iterable, key=lambda x: x):
    min_heap = []
    for element in iterable:
        heapq.heappush(min_heap, (key(element), element))
        if len(min_heap) > n:
            heapq.heappop(min_heap)
    return sorted([item[1] for item in min_heap], key=key, reverse=True)


def most_common(n: int, filename: str, chunk_size=1024, stop_words: Iterable = None):
    if stop_words is None:
        stop_words = []
    elements_count = defaultdict(int)
    Element = namedtuple("Element", "value count")

    with open(filename, 'r') as f:
        while text := f.read(chunk_size):
            text = re.sub(f"[{string.punctuation}]", '', text)
            words = text.lower().split()

            for word in words:
                elements_count[word] += 1

    for word in stop_words:
        elements_count.pop(word, None)

    top_n = [
        Element(value=item[0], count=item[1])
        for item in nlargest(n, elements_count.items(), key=lambda x: x[1])
    ]
    return top_n


def main():
    n = 10
    filename = "example.txt"
    top_n = most_common(n=n, filename=filename)

    print(f"Top {n} elements:")
    for element in top_n:
        print(f"{element.value} -> {element.count}")


if __name__ == "__main__":
    main()
