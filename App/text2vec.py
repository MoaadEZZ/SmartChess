import time
t1 = time.time()

from nltk.tokenize import TreebankWordTokenizer
from sklearn.preprocessing import LabelBinarizer
from gensim.models import Word2Vec
import numpy as np

print("Imports done in:", time.time() - t1, "seconds")

inputs = []
outputs = []

with open("document.txt") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        parts = line.split(" :: ")
        if len(parts) != 2:
            continue
        input_text, output_label = parts
        inputs.append(input_text)
        outputs.append(output_label)

tokenizer = TreebankWordTokenizer()
documents = []
vocabulary = set()

for line in inputs:
    tokens = [token.lower() for token in tokenizer.tokenize(line)]
    vocabulary.update(tokens)
    documents.append(tokens)

w2v_model = Word2Vec(documents, vector_size=100, window=5, min_count=1)

def get_sentence_embedding(sentence):
    tokens = [token.lower() for token in tokenizer.tokenize(sentence)]
    vectors = [w2v_model.wv[word] for word in tokens if word in w2v_model.wv]
    return np.mean(vectors, axis=0) if vectors else np.zeros(100)

X_w2v = np.array([get_sentence_embedding(" ".join(doc)) for doc in documents])

encoder = LabelBinarizer()
y_encoded = encoder.fit_transform(outputs)

count_output = {
    "play_chess": 0,
    "chat" : 0,
    "query_selection": 0
}
for e in outputs:
    count_output[e] += 1
    
print(count_output)
        
