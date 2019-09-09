import re 
import string 
import nltk 
from nltk.corpus import stopwords
from nltk import pos_tag, word_tokenize

dTrading = 'C:/Users/vitor/Documents/GetDataset/TradingView/'

ativos = ['aapl', 'abev', 'bbas', 'bbdc', 'brfs', 'btcusd', 'ciel', 'csna', 'ggbr', 'goll', 'ibov', 'itsa', 'itub', 'jbss', 'lame', 'ltcbrl', 'mglu', 'natu', 'petr', 'rent', 'usim', 'vale']
# ativos = ['abev']

def getImportanWords(c, d, ar, p, tipo):
    document_text = open(c + '2019-05-04/lexicon-sent-tf-oplexicon' + '.txt', 'r', encoding='utf8')
    f = document_text.readlines()
    arPos = []
    arNeg = []
    f1 = open(c + '2019-05-05/' + p + '-' + tipo + '.txt', 'a+')
    for dt in f:
        t = dt.split()
        try: 
            x = 'null'
            if t: 
                txt = t[0].split(';')
                if 'POL=-1' in txt[2]:
                    if str(txt[0]) not in arNeg:
                        arNeg.append(str(txt[0]))
                if 'POL=1' in txt[2]:
                    if str(txt[0]) not in arPos:
                        arPos.append(str(txt[0]))
        except IndexError:
                x = 'null' 
    

    for texto in ar:
        if tipo == 'pos':
            for word in arPos:
                if str(word) in texto and p in texto:
                    x = texto.count(word)
                    resp = str(word) + ';' + str(x) + '\n'
                    # print('Palavra: ' + str(word) + ' - Contagem: ' + str(x) + ' - Texto - ' + str(texto) + ' - ' + p) 
                    if str(word) not in open(dTrading + '2019-05-05/' + p + '-' + tipo + '.txt').read():
                        f1.write(resp)
        if tipo == 'neg':
            for word in arNeg:
                if str(word) in texto and p in texto:
                    x = texto.count(word)
                    resp = str(word) + ';' + str(x) + '\n'
                    # print('Palavra: ' + str(word) + ' - Contagem: ' + str(x) + ' - Texto - ' + str(texto) + ' - ' + p) 
                    f1.write(resp)
    f1.close

    return 'Ok'


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
                count += 1
                final = dt
                arrayW.append(final)
        getImportanWords(d, e, arrayW, p, f)
        # break
    return arrayW

runProcess(dTrading, '2019-05-04/positive', 'pos')
runProcess(dTrading, '2019-05-04/negative', 'neg')

# def runFile():
#     doc = open(dTrading + '2019-05-05/abev-neg.txt', 'r')
#     f1 = doc.readlines()
#     for t in f1:
#         txt = t.split(';')
#         for x in f1:
#             if t[0] in x:
#                 print(txt)
#         # print(txt)


# runFile()