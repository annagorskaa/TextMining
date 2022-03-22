import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

'''
    Return cleaned text

    :param text: original text
    :operation:
    :emoticons: retrieves emoticons from the text
    :text_low: sets lowercase letters
    :text_without_number: removes numbers
    :text_without_html: removes html tags
    :text_without_punc_marks: removes punctuation marks
    :text_without_white_space: removes multiple space
    :text_done: attaches emoticons to text

'''


def cleanup_text(text: str) -> str:
    emoticons = re.findall(r'[:|;][-]?[)|(|<>]', text)
    text_low = text.lower()
    text_without_number = re.sub(r'\d', '', text_low)
    text_without_html = re.sub(r'<.*?>', '', text_without_number)
    text_without_punc_marks = re.sub(r'\W(?<!\s)', '', text_without_html)
    text_without_white_space = text_without_punc_marks.strip()
    text_done = text_without_white_space + ' '.join(emoticons)
    return text_done


''' Return text without words from the list "stop_words" '''


def delete_stop_words(text: str) -> str:
    stop_words = stopwords.words("english")
    word_tokens = word_tokenize(text)
    filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
    return filtered_sentence
