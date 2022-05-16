import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from prettytable import PrettyTable
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

from text_function import text_tokenizer

true_posts = pd.read_csv('Data/True.csv', usecols=['title', 'text'])
fake_posts = pd.read_csv('Data/Fake.csv', usecols=['title', 'text'])


true = true_posts['title']
entire_text = ' '.join(true.to_list())
fake = fake_posts['title']
# tokens = text_tokenizer(entire_text)
# print(tokens)




vectorizer = CountVectorizer(tokenizer=text_tokenizer)
"""
    Operacje na pliku True
"""
X_transform = vectorizer.fit_transform(true)
slowa = vectorizer.get_feature_names_out(true)

m = sum(X_transform.toarray())
ind = np.argpartition(m, -10)[-10:]
print('Tokeny najczesciej wystepujace:')
print(slowa[ind])
print('Ilość najczesciej wystepujacych tokenów:')
print(m[ind])
# indeksy slowa najczesciej wystepujace
print(ind)

"""
    Najczęściej występujące tokeny w tytułach z pliku True
    Wizualizacja - wykres
"""
plt.barh(slowa[ind], m[ind], color='crimson')
plt.title('Najczęściej występujące tokeny w pliku True')
plt.ylabel('Ilość')
plt.xlabel('Termin')
plt.savefig('./Images/top_true.png')
plt.show()

"""
    Najczęściej występujące tokeny w tytułach z pliku True
    Wizualizacja - Pretty table
"""
columns = ["Termin","Ilość"]
newTable = PrettyTable()
newTable.add_column(columns[0], slowa[ind])
newTable.add_column(columns[1], m[ind])
newTable.sortby = columns[1]
print(newTable)


"""
    Operacje na pliku True
"""
X_transform = vectorizer.fit_transform(fake)
f_slowa = vectorizer.get_feature_names_out(fake)
f_sum = sum(X_transform.toarray())
f_ind = np.argpartition(f_sum, -10)[-10:]

print('Tokeny najczesciej wystepujace:')
print(f_slowa[f_ind])
print('Ilość najczesciej wystepujacych tokenów:')
print(f_sum[f_ind])
# indeksy slowa najczesciej wystepujace
print(f_ind)

"""
    Najczęściej występujące tokeny w tytułach z pliku True
    Wizualizacja - wykres
"""

plt.barh(f_slowa[f_ind], f_sum[f_ind], color='lightpink')
plt.title('Najczęściej występujące tokeny w pliku True')
plt.ylabel('Ilość')
plt.xlabel('Termin')
plt.savefig('./Images/top_fake.png')
plt.show()

"""
    Najczęściej występujące tokeny w tytułach z pliku Fake
    Wizualizacja - Pretty table
"""
columns = ["Termin","Ilość"]
newTable = PrettyTable()
newTable.add_column(columns[0], f_slowa[f_ind])
newTable.add_column(columns[1], f_sum[f_ind])
newTable.sortby = columns[1]
print(newTable)

"""
    Kluczowe tokeny tytułów z pliku True na podstawie miary TF - IDF
    top 10 najważniejszych tokenow
"""

tvectorizer = TfidfVectorizer(tokenizer=text_tokenizer)
TX_transform = tvectorizer.fit_transform(true)
# print(TX_transform.toarray())
top = sum(TX_transform.toarray())
ind2 = np.argpartition(top, -10)[-10:]
print(slowa[ind2])
print(top[ind2])
print(ind2)

"""
    Wizualizacja kluczowych tokenów tytułów z pliku True
"""
plt.barh(slowa[ind2], top[ind2], color='bisque')
plt.title('Kluczowe tokeny w pliku True')
plt.ylabel('TFIDF')
plt.xlabel('Termin')
plt.savefig('./Images/important10.png')
plt.show()

columns = ["Termin","TFIDF"]
newTable = PrettyTable()
newTable.add_column(columns[0], slowa[ind2])
newTable.add_column(columns[1], top[ind2])
newTable.sortby = columns[1]
print(newTable)


"""
    Top 10 dokumentów, które zawierają najwięcej tokenów
"""
n = np.sum(X_transform.toarray(), axis=1)
print(true[n])

"""
        10 najważniejszych tokenów na podstawie wagi binarnej
"""

vectorizer_bw = CountVectorizer(tokenizer=text_tokenizer, binary= True)

X_transform_bw = vectorizer_bw.fit_transform(true)
slowa_bw = vectorizer_bw.get_feature_names_out()
sum_bw = sum(X_transform_bw.toarray())
ind_bw = np.argpartition(sum_bw, -10)[-10:]

print(slowa_bw[ind_bw])
print(sum_bw[ind_bw])
print(ind_bw)

"""
    Wizualizacja  najważniejszych tokenów na podstawie wagi binarniej
"""

plt.barh(f_slowa[f_ind], f_sum[f_ind], color='springgreen')
plt.title('10 najważniejszych tokenów na podstawie wagi binarnej z pliku True')
plt.xlabel('Waga')
plt.ylabel('Termin')
plt.savefig('./Images/bw_top.png')
plt.show()

columns = ["Termin","Waga"]
newTable = PrettyTable()
newTable.add_column(columns[0], slowa[ind2])
newTable.add_column(columns[1], top[ind2])
newTable.sortby = columns[1]
print(newTable)
