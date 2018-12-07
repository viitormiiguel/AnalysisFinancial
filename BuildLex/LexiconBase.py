import sys 
import codecs
import nltk
from nltk.corpus import stopwords
from nltk import pos_tag, word_tokenize
import csv
import datetime
from collections import Counter
import re

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

def divideDataset(fonte):
    with open(fonte + today + '/dataset.csv', encoding="utf8") as dados:
        reader = csv.reader(dados)
        next(reader)
        d1 = [t for t in reader]
        f1 = open(fonte + today + '/positive.txt', 'w+', encoding="utf8")
        f2 = open(fonte + today + '/negative.txt', 'w+', encoding="utf8")
        f3 = open(fonte + today + '/neutral.txt', 'w+', encoding="utf8")
        for d in d1:
            try:
                if d[1] == 'Viés de alta':
                    d1 = preProcess(d[2])
                    f1.write(d1 + "\n")
                if d[1] == 'Viés de baixa':
                    d2 = preProcess(d[2])
                    f2.write(d2 + "\n")
                if d[1] == '':
                    d3 = preProcess(d[2])
                    f3.write(d3 + "\n")
            except IndexError:
                _ = 'null'
        f1.close()
        f2.close()
        f3.close()
        print("Arquivos gerados")

divideDataset(dTrading)

def openfile(filename):
    fh = open(filename, "r+", encoding='utf8')
    str = fh.read()
    fh.close()
    return str
 
def getwordbins(words):
    cnt = Counter()
    for word in words:
        cnt[word] += 1
    return cnt
 
def main(filename, topwords, tipo):
    txt = openfile(filename)
    words = txt.split(' ')
    bins = getwordbins(words)
    f1 = open(dTrading + today + '/lexicon-base.txt', 'a+', encoding="utf8")
    for key, value in bins.most_common(topwords):
        # print(key,value)
        # print(key)
        _ = value
        if tipo == 'n' and value > 10:
            f1.write(key + '\t\t' + '-1' + '\n')
        if tipo == 'p' and value > 10:
            f1.write(key + '\t\t' + '1' + '\n')
        if tipo == 'nt' and value > 10:
            f1.write(key + '\t\t' + '0' + '\n')
    f1.close()
    print("Lexicon created!")
 
main(dTrading + today + '/negative.txt', 500, 'n')
# main(dTrading + today + '/neutral.txt', 500, 'nt')
# main(dTrading + today + '/positive.txt', 500, 'p')
