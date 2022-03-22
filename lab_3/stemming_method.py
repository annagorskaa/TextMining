from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

''' Return stemming text as text '''


def stemming(text: str):
    stop_lista = stopwords.words("english")
    word_tokens = word_tokenize(text)
    words_without_stopwords = []
    for w in word_tokens:
        if w not in stop_lista:
            words_without_stopwords.append(w)

    ps = PorterStemmer()
    for word in words_without_stopwords:
        print("Temat słowa {} : {}".format(word, ps.stem(word)))


''' Return stemming text as list '''


def stemming_list(words_without_stopwords: str) -> list:
    ps = PorterStemmer()
    stem_list = []
    for word in words_without_stopwords:
        stem_list.append(ps.stem(word))
    return stem_list
