from wordcloud import WordCloud
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from nltk.tokenize import word_tokenize


def remove_stop_words(f):
    stop_words = ['Movie']
    for stop_word in stop_words:
        f = f.replace(stop_word, '')
    return f


# 生成词云
def create_word_cloud(f):
    print('根据词频，开始生成词云!')
    f = remove_stop_words(f)
    cut_text = word_tokenize(f)
    # print(cut_text)
    cut_text = " ".join(cut_text)
    wc_pic = WordCloud(
        max_words=100,
        width=2000,
        height=1200,
    )
    wc_res = wc_pic.generate(cut_text)
    # 写词云图片
    wc_res.to_file("wordcloud.jpg")
    # 显示词云文件
    plt.imshow(wc_res)
    plt.axis("off")
    plt.show()


if __name__ == '__main__':
    data = pd.read_csv('Market_Basket_Optimisation.csv', header=None)
    transactions = []
    for i in range(0, data.shape[0]):
        temp = []
        for j in range(0, 20):
            item = str(data.values[i, j])
            if item != 'nan':
                temp.append(item)
        transactions.append(temp)

    all_word = ''.join('%s' % item for item in transactions)
    print(all_word)
    create_word_cloud(all_word)
