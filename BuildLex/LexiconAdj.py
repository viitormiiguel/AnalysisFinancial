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

dTrading    = 'C:/Users/vitor/Documents/GetDataset/TradingView/'
sentilex    = open("Lexicon/SentiLex/SentiLex-lem-PT01.txt", 'r', encoding="utf8")
oplexicon   = open('Lexicon/OpLexicon/lexico_v2.txt', 'r', encoding="utf8")  
sentilex    = sentilex.readlines()
oplexicon   = oplexicon.readlines()

dic_palavra = {}

# def AdjLexico(base, arquivo):
#     lexico      = open(dTrading + today + base, 'r', encoding="utf8")
#     lexico      = lexico.readlines()
#     f1 = open(dTrading + today + arquivo, 'a+', encoding="utf8")
#     for line in lexico:
#         pos_spc = line.find('\t\t')
#         termo = (line[:pos_spc])
#         pol = (line[pos_spc:])
#         for i in sentilex:
#             pos_ponto = i.find('.')
#             palavra = (i[:pos_ponto])
#             pol_pos = i.find('POL')
#             polaridade = (i[pol_pos+4:pol_pos+6]).replace(';','')
#             pos_tag = i.find('PoS')
#             tag = (i[pos_tag+4:pos_tag+7])
#             dic_palavra[palavra] = polaridade
#             if termo == palavra:
#                 # print("TERMO: ", termo, " POSTAGGING: ", tag, " POL: ", pol)
#                 f1.write(termo + ';' + 'POS=' + tag + ';' + 'POL=' + pol)
#     f1.close()

def AdjLexico2(base, arquivo):
    lexico      = open(dTrading + today + base, 'r', encoding="utf8")
    lexico      = lexico.readlines()
    f1 = open(dTrading + today + arquivo, 'a+', encoding="utf8")
    for line in lexico:
        pos_spc = line.find(',')
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

def Stem():
    stemmer = nltk.stem.RSLPStemmer()
    lex     = open(dTrading + today + '/lexicon-sent-tf-oplexicon.txt', 'r', encoding="utf8")
    lex     = lex.readlines()
    f1 = open(dTrading + today + '/lexicon_complete.txt', 'a+', encoding="utf8")
    for line in lex:
        pos_ponto = line.find(';')
        palavra = (line[:pos_ponto])
        pos_tag = line.find('POS')
        tag = (line[pos_tag+4:pos_tag+7])
        pos_pol = line.find('POL=')
        pol = (line[pos_pol+4:pos_pol+7])
        pol = pol.replace(',','')
        s = stemmer.stem(palavra)
        f1.write(palavra + '.' + 'POS=' + tag + ';' + 'POL=' + pol + '\n')
        for i in sentilex:
            pos_ponto = i.find('.')
            p = (i[:pos_ponto])
            if re.match(r'^'+s, p):
                f1.write(p + '.' + 'POS=' + tag + ';' + 'POL=' + pol + '\n')
    f1.close()

def adjustFile():
    with open(dTrading + today + '/lexicon_complete.txt', 'r+', encoding="utf8") as fh:
        f1 = open('Lexicon/Finance/lexicon_final.txt', 'a+', encoding='utf8')
        f2 = open(dTrading + today + '/lexicon_final.txt', 'a+', encoding='utf8')
        for line in fh:
            if line.strip():
                r = line.strip() + "\n"
                f1.write(str(r))
                f2.write(str(r))
        f1.close()
        f2.close()

print("Lexicon match...")

# AdjLexico('/lexicon-tf-idf-1.txt', '/lexicon-sent-tf-sentilex.txt')
# AdjLexico('/lexicon-base.txt', '/lexicon-sent-base-sentilex.txt')

AdjLexico2('/lexicon-tf-idf-1.txt', '/lexicon-sent-tf-oplexicon.txt')
AdjLexico2('/lexicon-base.txt', '/lexicon-sent-base-oplexicon.txt')

print("Lexicon comparing...")

Stem()
adjustFile()

print("Lexicon Done!")

