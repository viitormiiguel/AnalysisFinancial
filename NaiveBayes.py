import csv 
import re 
import datetime
import re

from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob

now = datetime.datetime.now()
today = now.strftime("%Y-%m-%d")

dTrading = 'C:/Users/vitor/Documents/GetDataset/TradingView/'

with open(dTrading + today +'/dataset.csv', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    dataInfo = [r for r in reader]
    dataset = []
    for dados_tests in dataInfo:
        try: 
            if dados_tests[1]:
                x = dados_tests[1]
                y = dados_tests[2]
                dinside = (y, x)
                dataset.append(dinside)
        except IndexError:
            x = 'null'

train_set = dataset[:len(dataset)//2]
test_set = dataset[len(dataset)//2:]

cl = NaiveBayesClassifier(train_set)

accuracy = cl.accuracy(test_set)

frase = 'Após um bom período de acumulação, VALE3 finalmente rompeu os 56,00 com um belíssimo candle de alta, fechando praticamente na máxima da semana aos 61,00.  O papel agora tem como alvo a região dos 67,00.'

blob = TextBlob(frase,classifier=cl)

print('Esta frase é de caráter:{}'.format(blob.classify()))
print('Precisão da previsão:{}'.format(accuracy))

