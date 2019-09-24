# -*- coding: utf-8 -*-

import string
import nltk 
import re
import csv 
import datetime

from nltk.corpus import stopwords
from nltk import pos_tag, word_tokenize
from collections import Counter

dTrading = 'C:/Users/vitor/Documents/GetDataset/TradingView/'

now = datetime.datetime.now()
today = now.strftime("%Y-%m-%d")

def RemoveStopWords(instancia):
    instancia  = instancia.lower()
    stopwords = set(nltk.corpus.stopwords.words('portuguese'))
    palavras = [i for i in instancia.split() if not i in stopwords]
    return (" ".join(palavras))

def preProcess(frase):
    # Conversao para minusculos
    frase = frase.lower()
    # Remoção de numeros
    frase = re.sub('[-10-9]','', frase)
    # Remoçao de pontuação
    frase = re.sub(r'[-./?!,":;()\']','',frase)
    # Remoção de stopwords
    texto = RemoveStopWords(frase)
    return texto

def readFile(ativo):
    with open(dTrading + today + ativo + '.csv') as csvFile:
        readCSV = csv.reader(csvFile, delimiter=';')
        words = []
        for row in readCSV:
            if len(row) != 0 and 'Neutro' in row[1]:
                texto = preProcess(row[0])
                words.append(texto)
        countWord(words)

def countWord(texts):
    freq = {}
    for row in texts:
        print(row)
        count = freq.get(row, 0)
        freq[row] = count + 1
    freq_list = freq.keys()
    for words in freq_list:
        print(words + ' - ' + str(freq[words]))


readFile('/polaritySentiLexPre_ciel3')