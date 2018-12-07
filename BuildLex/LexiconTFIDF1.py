import sys 
import codecs
import nltk
from nltk.corpus import stopwords
from nltk import pos_tag, word_tokenize
import csv
import datetime
from collections import Counter
import re
import math
from textblob import TextBlob as tb

now = datetime.datetime.now()
today = now.strftime("%Y-%m-%d")

dTrading = 'C:/Users/vitor/Documents/GetDataset/TradingView/'

default_stopwords = set(nltk.corpus.stopwords.words('portuguese'))

def RemoveStopWords(instancia):
    instancia  = instancia.lower()
    stopwords = set(nltk.corpus.stopwords.words('portuguese'))
    palavras = [i for i in instancia.split() if not i in stopwords]
    return (" ".join(palavras))

def preProcess(txt):
    # Conversao para minusculos
    frase = txt.lower()
    # Remover urls
    frase = re.sub(r"http\S+", "", frase)
    # Remoção $ e %
    frase = re.sub('[R$%]','',frase)
    # Remoção de numeros
    frase = re.sub('[-10-9]','', frase)
    # Remoçao de pontuação
    frase = re.sub(r'[-./?!,":;()\']','',frase)
    # Remoção de stopwords
    frase = re.sub('[➖]','',frase)
    texto = RemoveStopWords(frase)
    return texto

# ---------------------------------------------------------------------------------
def tf(word, blob):
    return blob.words.count(word) / len(blob.words)

def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob.words)

def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))

def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf (word, bloblist)

def algo(b, t):
    f1 = open(dTrading + today + '/lexicon-tf-idf-1.txt', 'a+', encoding="utf8")
    for i, blob in enumerate(b):
        print("Top words in document {}".format(i + 1))
        scores = {word: tfidf(word, blob, b) for word in blob.words}
        sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        for word, score in sorted_words[:100]:
            print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))
            if t == 'n':
                f1.write(word + ',' + '-1' + '\n')
            if t == 'p':
                f1.write(word + ',' + '1' + '\n')
            if t == 'nt':
                f1.write(word + ',' + '0' + '\n')
    f1.close()

def divideDataset(fonte):
    bl1 = []
    bl2 = []
    bl3 = []
    doc1 = ""
    doc2 = ""
    doc3 = ""
    with open(fonte + today + '/dataset.csv', encoding="utf8") as dados:
        reader = csv.reader(dados)
        next(reader)
        d1 = [t for t in reader]        
        for d in d1:
            try:
                if d[1] == 'Viés de alta':
                    d1 = preProcess(d[2])
                    doc1 += "\n" + d1
                    t1 = tb(doc1)
                    bl1 = [t1]
                if d[1] == 'Viés de baixa':
                    d2 = preProcess(d[2])
                    doc2 += "\n" + d2
                    t2 = tb(doc2)
                    bl2 = [t2]
                if d[1] == '':
                    d3 = preProcess(d[2])
                    doc3 += "\n" + d3
                    t3 = tb(doc3)
                    bl3 = [t3]
            except IndexError:
                _ = 'null'
        algo(bl2, 'n')
        algo(bl1, 'p')
        algo(bl3, 'nt')

divideDataset(dTrading)

