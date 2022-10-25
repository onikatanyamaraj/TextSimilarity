import re
from collections import defaultdict


class Preparation(object):

    def __init__(self, path):
        self.path = path

    # 去掉词性标注，去掉虚词，只留下对文本辨识有贡献的词
    def data_cleaning(self):
        corpus = []
        with open(self.path, "r") as f:
            for line in f.readlines():
                line = re.sub("[^a-z]*/[u,w,f,p,k,c]", "", line)  # 考虑删去m
                line = re.sub("/[a-z,A-Z]*", "", line)
                line = line[21:]
                corpus.append(line)
        return corpus

    # 将一维句子数组转换为二维文章数组+去除在全部文章中的频率为1的词
    def get_articles(self, corpus):
        articles = []
        article = []
        for sentence in corpus:
            if len(sentence) == 0:
                articles.append(article)
                article = []
            else:
                wordbag = sentence.split()
                for i in wordbag:
                    article.append(i)
        articles.append(article)

        frequency = defaultdict(int)
        for article in articles:
            for token in article:
                frequency[token] += 1
        return [[token for token in article if frequency[token] > 1] for article in articles]