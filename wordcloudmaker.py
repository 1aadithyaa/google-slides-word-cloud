import json

from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt
import random

# import nltk
# from nltk.corpus import stopwords
# from nltk.stem import WordNetLemmatizer

# import string
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.cluster import KMeans

# def text_process(text):
#     '''
#     Takes in a string of text, then performs the following:
#     1. Remove all punctuation
#     2. Remove all stopwords
#     3. Return the cleaned text as a list of words
#     4. Remove words
#     '''
#     stemmer = WordNetLemmatizer()
#     nopunc = [char for char in text if char not in string.punctuation]
#     nopunc = ''.join([i for i in nopunc if not i.isdigit()])
#     nopunc =  [word.lower() for word in nopunc.split() if word not in stopwords.words('english')]
#     return [stemmer.lemmatize(word) for word in nopunc]

with open('slides.json', 'r') as f:
    slide_json = json.load(f)

words = []

# with open("slides.json", "rw") as f:
#     json.dump(slide_json)

# for slide in slide_json['slides'][7:]:
#     for key1, value1 in slide.items():
#         if key1 == 'pageElements':
#             page_element = value1[2]
#             for key2, value2 in page_element.items():
#                 if key2 == 'shape':
#                     for key3, value3 in value2.items():
#                         if key3 == 'text':
#                             for key4, value4 in value3.items():
#                                 if key4 == 'textElements':
#                                     for textElement in value4[1:6:2]:
#                                         for key5, value5 in textElement.items():
#                                             if key5 == 'textRun':
#                                                 for key6, value6 in value5.items():
#                                                     if key6 == 'content':
#                                                         words.append(value6[:-1])

for slide in slide_json['slides'][7:]:
    pageElements = slide['pageElements']
    page_element = pageElements[2]
    if 'shape' in page_element.keys():
        text = page_element['shape']['text']['textElements']
        for textElement in text[1:6:2]:
            if 'textRun' in textElement:
                content = textElement['textRun']['content']
                words.append(content[:-1])

# words = ['hello', 'hello', 'hello', 'hello', "goodbye", "what is this", "what is your mom", "how many times do i have to write this in order for you to listen"]


# tfidfconvert = TfidfVectorizer(ngram_range=(1,3)).fit(words)
# X_transformed=tfidfconvert.transform(words)

# modelkmeans = KMeans(n_clusters=3, init ='k-means++', n_init=93)
# modelkmeans.fit(X_transformed)

# Sum_of_squared_distances = []
# K = range(1,4)
# for k in K:
#     km = KMeans(n_clusters=k)
#     km = km.fit(X_transformed)
#     Sum_of_squared_distances.append(km.inertia_)
# plt.plot(K,Sum_of_squared_distances,'bx-')
# plt.xlabel('k')
# plt.ylabel('sum')
# plt.show()
    


wordcloud = WordCloud().generate(' '.join(words))

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
