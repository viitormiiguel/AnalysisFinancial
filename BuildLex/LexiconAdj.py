import sys 
import codecs
import nltk
from nltk.corpus import stopwords
from nltk import pos_tag, word_tokenize
import csv
import datetime
from collections import Counter
import re
import importlib
import imp

now = datetime.datetime.now()
today = now.strftime("%Y-%m-%d")

dTrading    = 'C:/Users/vitor/Documents/GetDataset/TradingView/'
sentilex    = open("Lexicon/SentiLex/SentiLex-lem-PT01.txt", 'r', encoding="utf8")
oplexicon   = open('Lexicon/OpLexicon/lexico_v2.txt', 'r', encoding="utf8")  
sentilex    = sentilex.readlines()
oplexicon   = oplexicon.readlines()

dic_palavra = {}

def AdjLexico(base, arquivo):
    lexico      = open(dTrading + today + base, 'r', encoding="utf8")
    lexico      = lexico.readlines()
    f1 = open(dTrading + today + arquivo, 'a+', encoding="utf8")
    for line in lexico:
        pos_spc = line.find('\t\t')
        termo = (line[:pos_spc])
        pol = (line[pos_spc:])
        for i in sentilex:
            pos_ponto = i.find('.')
            palavra = (i[:pos_ponto])
            pol_pos = i.find('POL')
            polaridade = (i[pol_pos+4:pol_pos+6]).replace(';','')
            pos_tag = i.find('PoS')
            tag = (i[pos_tag+4:pos_tag+7])
            dic_palavra[palavra] = polaridade
            if termo == palavra:
                # print("TERMO: ", termo, " POSTAGGING: ", tag, " POL: ", pol)
                f1.write(termo + ';' + 'POS=' + tag + ';' + 'POL=' + pol)    
    for line in lexico:
        pos_spc = line.find('\t\t')
        termo = (line[:pos_spc])
        pol = (line[pos_spc:])
        for i in oplexicon:
            pos_ponto = i.find(',')
            palavra = (i[:pos_ponto])
            pos_tag = i.find(',')
            tag = (i[pos_tag+1:pos_tag+4])
            if termo == palavra:
                # print("TERMO: ", termo, " POSTAGGING: ", tag, " POL: ", pol)
                f1.write(termo + ';' + 'POS=' + tag + ';' + 'POL=' + pol)    
    f1.close()

AdjLexico('/lexicon-tf-idf-1.txt', '/lexicon-sent-1.txt')
AdjLexico('/lexicon-base.txt', '/lexicon-sent-2.txt')
