from typing import List
from time import time


def calculate_time(function):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = function(*args, **kwargs)
        end_time = time()
        print(f"total time: {end_time - start_time}")
        return result

    return wrapper


@calculate_time
def median(numbers: List[int]):
    numbers = sorted(numbers)
    length = len(numbers)
    if length == 0:
        raise ValueError("List cannot be empty")
    elif length % 2 == 0:
        return (numbers[length//2] + numbers[length//2 - 1]) / 2
    else:
        return numbers[len(numbers)//2]


if __name__ == "__main__":
    print(median([1, 2, 3]))
