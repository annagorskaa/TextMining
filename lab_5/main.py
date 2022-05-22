import pandas as pd
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, BaggingClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

import text_function as tfun
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split

"""
    Pobranie i przygotowanie zbioru danych
"""
true_post = pd.read_csv('./data/True.csv', usecols=['title'])
true_post['type'] = 'True'

fake_post = pd.read_csv('./data/Fake.csv', usecols=['title'])
fake_post['type'] = 'Fake'

result = pd.concat([true_post, fake_post])


"""
    Podział danych na zestaw uczący i zestaw testowy
    ( 30% danych przeznaczone jako zbiór do testowowania, pozostałe 70% do uczenia modelu )
    o ziarnie losowości równym 1.
"""
X = result['title']
y = result['type']

X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.3, random_state=1)


"""
    Wektoryzacja z użyciem CountVectorizera
"""

vectorizer = CountVectorizer(tokenizer=tfun.text_tokenizer)
X_train_transform = vectorizer.fit_transform(X_train)
X_test_transform = vectorizer.transform(X_test)

"""
    Pojedyncze drzewo decyzyjne
"""

tree = DecisionTreeClassifier()
tree = tree.fit(X_train_transform, Y_train)
print("Dokładność w zestawie uczącym drzewo decyzyjne: {:.3f}".format(tree.score(X_train_transform, Y_train)))
print("Dokładność w zestawie testowym drzewo decyzyjne: {:.3f}".format(tree.score(X_test_transform, Y_test)))

"""
   Lasy losowe
"""

forest = RandomForestClassifier(n_estimators=5, random_state=2)
forest = forest.fit(X_train_transform, Y_train)
print("Dokładność w danych uczących las losowy: {:.3f}".format(forest.score(X_train_transform, Y_train)))
print("Dokładność w danych testowych las losowy: {:.3f}".format(forest.score(X_test_transform, Y_test)))


"""
   SVM
"""

svml = SVC()
svml = svml.fit(X_train_transform, Y_train)
print("Dokładność w danych uczących SVM: {:.3f}".format(svml.score(X_train_transform, Y_train)))
print("Dokładność w danych testowych SVM: {:.3f}".format(svml.score(X_test_transform, Y_test)))

"""
   AdaBoost
"""

ada = AdaBoostClassifier()
ada = ada.fit(X_train_transform, Y_train)
print("Dokładność w danych uczących AdaBoostClassifier: {:.3f}".format(ada.score(X_train_transform, Y_train)))
print("Dokładność w danych testowych AdaBoostClassifier: {:.3f}".format(ada.score(X_test_transform, Y_test)))

"""
   BaggingClassifier
"""
bagg = BaggingClassifier()
bagg = bagg.fit(X_train_transform, Y_train)
print("Dokładność w danych uczących BaggingClassifier: {:.3f}".format(bagg.score(X_train_transform, Y_train)))
print("Dokładność w danych testowych BaggingClassifier: {:.3f}".format(bagg.score(X_test_transform, Y_test)))


# Rezultat:
# Dokładność w zestawie uczącym drzewo decyzyjne: 1.000
# Dokładność w zestawie testowym drzewo decyzyjne: 0.895
# Dokładność w danych uczących las losowy: 0.990
# Dokładność w danych testowych las losowy: 0.912
# Dokładność w danych uczących SVM: 0.986
# Dokładność w danych testowych SVM: 0.943
# Dokładność w danych uczących BaggingClassifier: 0.992
# Dokładność w danych testowych BaggingClassifier: 0.909