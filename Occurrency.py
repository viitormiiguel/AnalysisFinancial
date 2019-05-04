import re 
import string 
import nltk 
from nltk.corpus import stopwords
from nltk import pos_tag, word_tokenize

dTrading = 'C:/Users/vitor/Documents/GetDataset/TradingView/'

ativos = ['aapl', 'abev', 'bbas', 'bbdc', 'brfs']

def runProcess(d, e, f):
    doc = open(d + e + '.txt', 'r', encoding='utf8')
    f1 = doc.readlines()
    arrayW = []
    for p in ativos:
        count = 0
        p = p.lower()
        for dt in f1:
            dt = dt.lower()
            dt = dt.replace('\n', '')
            if str(p) in dt: 
                print(p)
                print(dt)
    return arrayW

runProcess(dTrading, '2019-05-04/positive', '')