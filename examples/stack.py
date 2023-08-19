class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def is_empty(self) -> bool:
        return len(self.stack) == 0

    def peek(self):
        return self.stack[-1]

    def length(self) -> int:
        return len(self.stack)


def is_balanced(string: str) -> bool:
    stack = Stack()
    for letter in string:
        if letter == "(":
            stack.push(letter)
        elif letter == ")":
            if stack.is_empty():
                return False
            else:
                stack.pop()

    if stack.is_empty():
        return True
    else:
        return False


def reverse(string: str) -> str:
    stack = Stack()
    for letter in string:
        stack.push(letter)

    result = ""
    for _ in range(stack.length()):
        result += stack.pop()

    return result


def to_binary(number: int) -> int:
    stack = Stack()
    divisor = 2
    while number >= divisor:
        stack.push(number % divisor)
        number //= divisor

    stack.push(number)

    result = ""
    for _ in range(stack.length()):
        result += str(stack.pop())
    return int(result)


if __name__ == "__main__":
    print(is_balanced("(("))  # False
    print(is_balanced("(())"))  # True
    print(is_balanced("(()())"))  # True
    print(is_balanced("(()"))  # False
    print(is_balanced(")"))  # False
    print(is_balanced(""))  # True

    print(reverse(""))
    print(reverse("amir"))
    print(reverse("a"))

    print(to_binary(12))  # 1100
    print(to_binary(1))  # 1
    print(to_binary(2))  # 10
