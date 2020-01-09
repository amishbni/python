from wordcloud import WordCloud, STOPWORDS

with open("test.txt", 'r') as input_file:
    text = input_file.read()

stopwords = set(STOPWORDS)

wc = WordCloud(background_color="white", max_words=2000,
        width=1024, height=1024,
        stopwords=stopwords, contour_width=3, contour_color="steelblue")

wc.generate(text)

wc.to_file("wordcloud.png")

