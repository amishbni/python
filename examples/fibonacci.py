from time import time


def timer(function):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = function(*args, **kwargs)
        end_time = time()
        print(f"{end_time - start_time:.10f}", end=" seconds. ")
        return result
    return wrapper


@timer
def fibonacci(n, method="iterative"):
    def recursive(number):
        if number < 2:
            return number
        return recursive(number - 1) + recursive(number - 2)

    def iterative(number):
        if number < 2:
            return number
        a, b = 0, 1
        for _ in range(number):
            a, b = b, a+b
        return a

    def cached(number, computed={0: 0, 1: 1}):
        if number not in computed:
            computed[number] = cached(number - 1, computed) + cached(number - 2, computed)
        return computed[number]

    return locals()[method](n)


if __name__ == "__main__":
    for i in range(1, 101):
        print(f"fibonacci({i}) = {fibonacci(i, method='cached')}")
