import re

text = "ادبیات فارسی    ۱۹.۵"
pattern = r"([ا-ی‌ ]+)    ([۰-۹]+(.[۰-۹]+)?)"

if(match := re.match(pattern, text)):
    print(match.groups())
else:
    print("No")
