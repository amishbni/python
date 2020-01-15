from wordcloud import WordCloud
from collections import Counter
from pprint import pprint
import sys, os

args = sys.argv

if len(args) == 1:
    print("Specify a text file, so I can generate a world cloud for!")
    exit(1)

filepath = args[1]

with open(filepath, 'r') as input_file:
    commands = input_file.read().split()

most_common = Counter(commands).most_common()
freq = dict(most_common)

wc = WordCloud(
    background_color="white",
    max_words=2000,
    width=2048, height=2048,
    normalize_plurals=False)

wc.generate_from_frequencies(freq)

output_file_name = os.path.basename(os.path.normpath(filepath)).split('.')[0]

wc.to_file(f"{output_file_name}.png")

