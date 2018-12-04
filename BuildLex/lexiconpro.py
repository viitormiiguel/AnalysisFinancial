import sys 
import imp
import importlib
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

dTrading    = 'C:/Users/vitor/Documents/GetDataset/TradingView/'
sentilex    = open("Lexicon/SentiLex/SentiLex-lem-PT01.txt", 'r', encoding="utf8")
lexico      =  open(dTrading + today + '/lexicon.txt', 'r', encoding="utf8") 

dic_palavra = {}
for i in sentilex.readlines():
    pos_ponto = i.find('.')
    palavra = (i[:pos_ponto])
    pol_pos = i.find('POL')
    polaridade = (i[pol_pos+4:pol_pos+6]).replace(';','')
    dic_palavra[palavra] = polaridade    

for line in lexico.readlines():
    pos_spc = line.find('\t\t')
    termo = (line[:pos_spc])
    if termo in sentilex.readlines():
        print(termo)

