# Most Common Words
from collections import Counter
from pprint import pprint
import sys

args = sys.argv

if len(args) == 1:
    print("Specify the file path")
    exit(1)

filepath = args[1]

text = ""

with open(filepath, 'r') as input_file:
    text = input_file.read()

commands = text.split()

counter = Counter(commands)

pprint(counter.most_common(25))
