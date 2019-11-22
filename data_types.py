# Fundamental data types in Python
data_types = [int, float, bool, str, list, tuple, set, dict]

for data_type in data_types:
    print(data_type)
                                        # <class 'int'>
                                        # <class 'float'>
                                        # <class 'bool'>
                                        # <class 'str'>
                                        # <class 'list'>
                                        # <class 'tuple'>
                                        # <class 'set'>
                                        # <class 'dict'>

# None, absence of a value
print(type(None))                       # <class 'NoneType'>

# int data type
print(2 + 4)                            # 6
print(2 - 4)                            # -2
print(2 * 4)                            # 8
print(2 / 4)                            # 0.5
print(2 // 4)                           # 0
print(2 % 4)                            # 2
print(2 ** 4)                           # 16

# float arithmetic
one_tenth = .1
print(one_tenth)                        # 0.1
print(one_tenth * 3)                    # 0.30000000000000004

three_tenth = one_tenth * 3
print(three_tenth)                      # 0.30000000000000004
print(three_tenth == .3)                # False
print(round(one_tenth, 1) * 3 == .3)    # False
print(round(three_tenth, 1) == .3)      # True


# as_integer_ratio() method
pi_5 = 3.14159
print(pi_5)                             # 3.14159

pi_5_ratio = pi_5.as_integer_ratio()
print(pi_5_ratio)                       # (3537115888337719, 1125899906842624)

divided = pi_5_ratio[0] / pi_5_ratio[1]
print(divided)                          # 3.14159

print(divided == pi_5)                  # True