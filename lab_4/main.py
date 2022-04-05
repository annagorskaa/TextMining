import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

from text_function import text_tokenizer

true_posts = pd.read_csv('Data/True.csv', usecols=['title', 'text'])

# true = true_posts['title'].sample(10)
true = true_posts['title'][:20]
entire_text = ' '.join(true.to_list())
# tokens = text_tokenizer(entire_text)
# print(tokens)


vectorizer = CountVectorizer(tokenizer=text_tokenizer)

X_transform = vectorizer.fit_transform(true)
# print(X_transform.toarray())
slowa = vectorizer.get_feature_names_out(true)


m = sum(X_transform.toarray())
ind = np.argpartition(m, -10)[-10:]
# slowa najczesciej wystepujace
print(slowa[ind])
# ilosc najczesciej wystepujacych slowa
print(m[ind])
# indeksy slowa najczesciej wystepujace
print(ind)

# top 10 najwazniejszych tokenow
tvectorizer = TfidfVectorizer(tokenizer=text_tokenizer)
TX_transform = vectorizer.fit_transform(true)
# print(TX_transform.toarray())
naj = sum(TX_transform.toarray())
ind2 = np.argpartition(naj, -10)[-10:]
print(slowa[ind2])
print(naj[ind2])
print(ind2)

# zadanie 4 top 10 dokumentow, ktore zawieraja najwiecej tokenow
n = np.sum(X_transform.toarray(), axis=1)
print(true[n])
