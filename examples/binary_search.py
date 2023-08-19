from typing import List


def binary_search(numbers: List[int], target: int):
    left, right = 0, len(numbers) - 1
    while left <= right:
        middle = (left + right) // 2
        middle_element = numbers[middle]
        if middle_element == target:
            return middle
        elif middle_element < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1


if __name__ == "__main__":
    print(binary_search([1, 4, 5, 7, 8, 10, 15], 10))  # 5
    print(binary_search([1, 4, 5, 7, 8, 10, 15], 4))  # 1
    print(binary_search([1, 4, 5, 7, 8, 10, 15], 7))  # 3
    print(binary_search([1, 4, 5, 7, 8, 10, 15], 19))  # -1
