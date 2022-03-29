import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

from text_function import text_tokenizer

true_posts = pd.read_csv('Data/True.csv', usecols=['title', 'text'])

true = true_posts['title'].sample(10)
entire_text = ' '.join(true.to_list())
tokens = text_tokenizer(entire_text)
print(tokens)

# vectorizer = TfidfVectorizer(tokenizer=text_tokenizer)
# X_transform = vectorizer.fit_transform(true)
# print(np.asarray(X_transform))

vectorizer = CountVectorizer(tokenizer=text_tokenizer)
X_transform = vectorizer.fit_transform(true)

print(X_transform.toarray())
