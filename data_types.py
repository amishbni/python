# Fundamental data types in Python
data_types = [int, float, bool, str, list, tuple, set, dict]

for data_type in data_types:
    print(data_type)

# None, absence of a value
print(type(None))

# int data type
print(f"2 + 4 is {2 + 4}")
print(f"2 - 4 is {2 - 4}")
print(f"2 * 4 is {2 * 4}")
print(f"2 / 4 is {2 / 4}")
print(f"2 // 4 is {2 // 4}")
print(f"2 % 4 is {2 % 4}")
print(f"2 ** 4 is {2 ** 4}")

# float arithmetic
one_tenth = .1
print(one_tenth)                        # 0.1
print(one_tenth * 3)                    # 0.30000000000000004

three_tenth = one_tenth * 3
print(three_tenth)                      # 0.30000000000000004
print(three_tenth == .3)                # False
print(round(one_tenth, 1) * 3 == .3)    # False
print(round(three_tenth, 1) == .3)      # True
