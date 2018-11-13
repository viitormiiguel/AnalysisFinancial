import nltk
import re 
import nltk
import csv
import datetime
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import math

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
    # Remoção de numeros
    frase = re.sub('[-10-9]','', frase)
    # Remoçao de pontuação
    frase = re.sub(r'[-./?!,":;()\']','',frase)
    # Remoção de stopwords
    texto = RemoveStopWords(frase)
    return texto

def removeSpecialCharacters(s):
    stripped = re.sub('[^\w\s]','',s)
    stripped = re.sub('_','',stripped)
    stripped = re.sub('\s+',' ', stripped)
    stripped = stripped.strip()
    return stripped

def get_doc(sent):
    doc_info = []
    i = 0
    for sent in text_sents_clean:
        i += 1
        count = count_words(sent)
        temp = {'doc_id': i, 'doc_length' : count}
        doc_info.append(temp)
    return doc_info

def count_words(sent):
    count = 0
    words = word_tokenize(sent)
    for word in words:
        count += 1
    return count

def create_freq_dict(sents):
    i = 0
    freqDict_list = []
    f1 = open(dTrading + today + '/lexicon.txt', 'a+', encoding="utf8")
    teste = []
    for sent in sents:
        i += 1
        freq_dict = {}
        words = word_tokenize(sent)
        for t in words:
            if not t in teste:
                teste.append(t)
        for word in words:
            word = word.lower()
            if word in freq_dict:
                freq_dict[word] += 1
            else:
                freq_dict[word] = 1
            temp = {'doc_id' : i, 'freq_dict': freq_dict}
        freqDict_list.append(temp)
    
    for new in teste:
        # f1.write(new + '\t\t' + '-1'+ '\n')
        f1.write(new + '\t\t' + '0'+ '\n')
        # f1.write(new + '\t\t' + '1'+ '\n')
    f1.close()
    return freqDict_list

def computeTF(doc_info, freqDict_list):
    TF_scores = []
    for tempDict in freqDict_list:
        id = tempDict['doc_id']
        for k in tempDict['freq_dict']:
            temp = {'doc_id': id,
                    'TF_score': tempDict['freq_dict'][k]/doc_info[id-1]['doc_length'],
                    'key': k}
            TF_scores.append(temp)
    return TF_scores

def computeIDF(doc_info, freqDict_list):
    IDF_scores = []
    counter = 0
    for dict in freqDict_list:
        counter += 1
        for k in dict['freq_dict'].keys():
            count = sum([k in tempDict['freq_dict'] for tempDict in freqDict_list])
            temp = {'doc_id': counter, 'IDF_score': math.log(len(doc_info)/count), 'key' : k}
            IDF_scores.append(temp)
    return IDF_scores

def computeTFIDF(TF_scores, IDF_scores):
    TFIDF_scores = []
    for j in IDF_scores:
        for i in TF_scores:
            if j['key'] == i['key'] and j['doc_id'] == i['doc_id']:
                temp = {'doc_id' : j['doc_id'],
                        'TFIDF_score' : j['IDF_score']*i['TF_score'],
                        'key' : i['key']}
        TFIDF_scores.append(temp)
    return TFIDF_scores

def divideDataset(fonte):
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
                if d[1] == 'Viés de baixa':
                    d2 = preProcess(d[2])
                    doc2 += "\n" + d2
                if d[1] == '':
                    d3 = preProcess(d[2])
                    doc3 += "\n" + d3
            except IndexError:
                _ = 'null'
        return doc1

texto = divideDataset(dTrading)

text_sents = sent_tokenize(texto)
text_sents_clean = [removeSpecialCharacters(s) for s in text_sents]
doc_info = get_doc(text_sents_clean)

freqDict_list = create_freq_dict(text_sents_clean)
TF_scores = computeTF(doc_info, freqDict_list)
IDF_scores = computeIDF(doc_info, freqDict_list)
TFIDF_scores = computeTFIDF(TF_scores, IDF_scores )

# print(doc_info)
# print(freqDict_list)
# print(TF_scores)