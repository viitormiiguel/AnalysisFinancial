import re
import string
import nltk
from nltk.corpus import stopwords
from nltk import pos_tag, word_tokenize

dTrading    = 'C:/Users/vitor/Documents/GetDataset/TradingView/'

ativos = ['aapl', 'abev', 'bbas', 'bbdc', 'brfs', 'btusd', 'ciel', 'csna', 'ggbr', 'goll', 'ibov',
'itsa', 'itub', 'jbss', 'lame', 'ltcbrl', 'mglu', 'natu', 'petr', 'rent', 'usim', 'vale']

def getImportanWords(c, d, e, p):
        # document_text = open(c + d + '.txt', 'r')
        arrayWords = []
        print(e)
        f1 = open(c + '2019-05-04/' + p + '.txt', 'a+')
        # for dt in document_text.readlines():
        #         t = dt.split()
        #         # print(t)
        #         try: 
        #                 x = 'null'
        #                 if t: 
        #                         txt = t[1][0:len(t[1])-4]
        #                         t1 = t[0][2:len(t[0])-1]
        #                         t1 = t1.replace("'","")

        #                         t2 = str(t[1][5:])
        #                         t2 = t2[t2.find(','):]
        #                         t2 = t2[1:]

        #                         if txt.find('JJ') == 1: 
        #                                 if int(t2) > 100:
        #                                         arrayWords.append(t1)
        #         except IndexError:
        #                 x = 'null'

        # contagem = 0
        # # print('\n')
        # # print(q)
        # for word in arrayWords:
        #         for texto in p:
        #                 if word in texto and vip in texto:
        #                         contagem += 1        
        #         # print('Palavra: ' + word + ' contagem ' + str(contagem) + ' personagem: ' + vip)
        #         # resp = 'Palavra: ' + word + ' contagem ' + str(contagem) + ' personagem: ' + vip + '\n'
        #         resp = word + ';' + str(contagem) + ';' + vip + '\n'
        #         f1.write(resp)
        f1.close

        return arrayWords

def runProcess(d, e, f):
        doc = open(d + e + '.txt', 'r', encoding='utf8')
        arrayW = []
        for p in ativos:
                count = 0
                p = p.lower()
                for dt in doc.readlines():
                        dt = dt.lower()
                        dt = dt.replace('\n','')
                        if str(p) in dt:
                                print(p)
                                print(dt)
        return arrayW

runProcess(dTrading, '2019-05-04/positive', 'teste')