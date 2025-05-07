import time
t1 = time.time()
from nltk.tokenize import TreebankWordTokenizer
from sklearn.feature_extraction.text import TfidfVectorizer
from gensim.models import Word2Vec
import numpy as np
print(time.time()-t1)

with open("document.txt") as f:
    corpus = []
    for x in f:
        corpus.append(x)

tokenizer = TreebankWordTokenizer()
documents = []
vocabulary = []
for e in corpus:
    x = tokenizer.tokenize(e)
    for i in range(0, len(x)):
        x[i] = x[i].lower()
        if x[i] not in vocabulary:
            vocabulary.append(x[i])
    documents.append(x)

w2v_model = Word2Vec([text.split() for text in corpus], vector_size=100, window=5, min_count=1)

def get_sentence_embedding(sentence):
    words = sentence.split()
    vectors = [w2v_model.wv[word] for word in words if word in w2v_model.wv]
    return np.mean(vectors, axis=0) if vectors else np.zeros(100)

X_w2v = np.array([get_sentence_embedding(text) for text in corpus])


