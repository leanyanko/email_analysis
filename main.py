import numpy as np
import pandas as pd

s = pd.Series([1, 3, 5, np.nan, 6, 8])

from io import StringIO

import string
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.stem.porter import PorterStemmer

# Remove punctuation signs
def remove_punctuations(text):
    for punctuation in string.punctuation:
        text = text.replace(punctuation, '')
        # text = re.sub(r'[^a-zA-Z]', ' ', text)   #unsure yet if I want that
    return text

# Remove stop words
def remove_stop(text):
    stop = set(stopwords.words('english'))
    filtered_sentence = [w for w in text if not w in stop]
    return filtered_sentence

# Stem words
def stem(text):
    porter = PorterStemmer()
    text = [porter.stem(token) for token in text]
    return text


def main():
    with open('content_cleaned.csv', 'r') as csvfile:
        data = csvfile.read()
        df = pd.read_csv(StringIO(data))
    df["content"] = df["content"].apply(remove_punctuations)
    df["content"] = df["content"].apply(word_tokenize)
    df["content"] = df["content"].apply(remove_stop)
    df["content"] = df["content"].apply(stem)
    print(df);

main()


