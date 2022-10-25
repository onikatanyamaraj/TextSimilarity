from preparation import Preparation
from gensim import corpora, models, similarities
from gensim.summarization.bm25 import BM25

if __name__ == '__main__':
    ss = Preparation(r"C:\\Users\\WINTOUR\\Desktop\\199801_clear .txt")
    corpus = ss.data_cleaning()
    articles = ss.get_articles(corpus)
    dictionary = corpora.Dictionary(articles)
    bow_corpus = [dictionary.doc2bow(article) for article in articles]

    # 获取tfidf模型
    tfidf = models.TfidfModel(bow_corpus)
    index = similarities.MatrixSimilarity(tfidf[bow_corpus], num_features=tfidf.num_nnz)
    res_tfidf= []
    for i in range(3579):
        res_tfidf.append(index[tfidf[bow_corpus[i]]])

    # 获取bm25模型
    bm25 = BM25(articles)
    res_bm25 = []
    for i in range(3579):
        res_bm25.append(bm25.get_scores(articles[i]))

    # 输出矩阵
    # print(res_tfidf)
    print(res_bm25)
