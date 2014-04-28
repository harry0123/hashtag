#!/usr/bin/python

import pandas as pd
import re
from collections import Counter

DATA_PATH = "/home/ubuntu/hashtag/"

tweets = pd.read_csv(DATA_PATH+'tweets.csv', low_memory=False).drop_duplicates()

def simple_tokenize(string):
    split_regex = r'\W+'
    return filter(None, re.split(split_regex, string.lower()))

stopwords = [line.rstrip() for line in open(DATA_PATH + "stopwords.txt", 'r')] # Load from file

def simple_tokenize(string):
    split_regex = r'\W+'
    return filter(None, re.split(split_regex, string.lower()))

def tokenize(string):
    return [word for word in simple_tokenize(string) if word not in stopwords]

#tokenize text in dataframe
tweets['text'] = tweets['text'].apply(tokenize)

def tf(tokens):
    total = float(len(tokens))
    count = Counter()
    for word in tokens:
        count[word] += 1
    count = dict(count)
    for word in count:
        count[word] = float(count[word]) / total
    return count

tweets['tf'] = tweets['text'].apply(tf)
print tweets.head()
