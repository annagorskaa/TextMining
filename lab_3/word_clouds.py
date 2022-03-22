from wordcloud import WordCloud
import pandas
import clean_text as ct
import stemming_method as st_m
import matplotlib.pyplot as plt


def chmury_slow(sciezka: str):
    teksty = pandas.read_csv(sciezka, usecols=['title', 'text'], encoding='UTF-8')
    teksty = teksty.sample(20)
    teksty = ''.join(teksty['title'])
    cleaned = ct.cleanup_text(teksty)
    deleted = ct.delete_stop_words(cleaned)
    stem = st_m.stemming_list(deleted)
    uniques = list(set(stem))
    bow = {unique: stem.count(unique) for unique in uniques}
    wc = WordCloud(width=3000, height=2000, background_color='white', colormap='PiYG')
    chmura = wc.generate_from_frequencies(bow)
    # plt.figure()
    plt.axis("off")
    plt.imshow(chmura, interpolation='bilinear')
    plt.show()
