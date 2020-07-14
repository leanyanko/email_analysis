import numpy as np
import pandas as pd

s = pd.Series([1, 3, 5, np.nan, 6, 8])

from io import StringIO

import string
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.stem.porter import PorterStemmer
from gensim import corpora
from gensim import models
import pickle
from nltk.stem.wordnet import WordNetLemmatizer

# Remove punctuation signs
def remove_punctuations(text):
    for punctuation in string.punctuation:
        text = text.replace(punctuation, '')
        # text = re.sub(r'[^a-zA-Z]', ' ', text)   #unsure yet if I want that
    return text

# Remove stop words
def remove_stop(text):
    stop = stopwords.words('english')
    filtered_sentence = [w for w in text if not w in stop]
    return filtered_sentence

# Lemmatize words
def lem(text):
    lemma = WordNetLemmatizer()
    text = [lemma.lemmatize(word) for word in text]
    return text

# Stem words
def stem(text):
    porter = PorterStemmer()
    text = [porter.stem(token) for token in text]
    return text

# Find topics for each email with gensim
def find_topic(arr):
    text_data = [a.split() for a in arr]
    if len(text_data) < 1:
        print(0)
        return ""
    dictionary = corpora.Dictionary(text_data)
    # print(dictionary)
    corpus = [dictionary.doc2bow(text) for text in text_data]
    pickle.dump(corpus, open('corpus.pkl', 'wb'))
    dictionary.save('dictionary.gensim')
    ldamodel = models.ldamodel.LdaModel(corpus, num_topics=1, id2word=dictionary, passes=15)
    ldamodel.save('model5.gensim')
    topics = ldamodel.print_topics(num_words=4)
    # for topic in topics:
    #     print(topic)
    print(topics[0])
    return ldamodel.get_topics()

# Parse topics for visualization
def parseForVis(topics):
    cleaned = topics.split(' ')


def main():
    with open('content_cleaned.csv', 'r') as csvfile:
        data = csvfile.read()
        df = pd.read_csv(StringIO(data))
    df["content"] = df["content"].apply(remove_punctuations)
    df["content"] = df["content"].apply(word_tokenize)
    df["content"] = df["content"].apply(remove_stop)
    df["content"] = df["content"].apply(lem)
    df["content"] = df["content"].apply(stem)
    df["topics"] = df["content"].apply(find_topic)
    print(df)
main()


