from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances, cosine_distances
import text_function as textfun
import pandas as pd

df = pd.read_excel('Data/example.xlsx')
sentence = df['Sentence']
print(sentence)

vectorizer = CountVectorizer(tokenizer=textfun.text_tokenizer)
X_transform = vectorizer.fit_transform(sentence)

ed = euclidean_distances(X_transform, X_transform)
cs = cosine_similarity(X_transform, X_transform)
cd = cosine_distances(X_transform, X_transform)

print('Euclidean distances: \n', ed)
print('Cosine similarity: \n', cd)
print('Cosine distances: \n', cs)