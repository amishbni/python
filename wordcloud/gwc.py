from wordcloud import WordCloud, STOPWORDS
import sys, os

args = sys.argv

if len(args) == 1:
    print("Specify a text file, so I can generate a world cloud for!")
    exit(1)

filepath = args[1]

with open(filepath, 'r') as input_file:
    text = input_file.read()

stopwords = set(STOPWORDS)

wc = WordCloud(background_color="white", max_words=2000,
        width=1024, height=1024,
        stopwords=stopwords, contour_width=3, contour_color="steelblue")

wc.generate(text)

output_file_name = os.path.basename(os.path.normpath(filepath)).split('.')[0]

wc.to_file(f"{output_file_name}.png")

