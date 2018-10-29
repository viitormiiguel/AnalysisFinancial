import csv 
import re 
import datetime
import re
import imp

from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob

now = datetime.datetime.now()
today = now.strftime("%Y-%m-%d")

dInfoMoney = 'C:/Users/vitor/Documents/GetDataset/Infomoney/'
dInvesting = 'C:/Users/vitor/Documents/GetDataset/Investing.com/'
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

# Treinando classificador 
cl = NaiveBayesClassifier(train_set)
#Testando Classificador
accuracy = cl.accuracy(test_set)

def RunAnalysis(fonte, tipo):
    with open(fonte + today +'/dataset.csv', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        data1 = [r for r in reader]
    with open(fonte + today +'/' + tipo + '.csv', mode='w', encoding="utf8") as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)    
        for listagem in data1:
            try:
                blob = TextBlob(listagem[2], classifier=cl)
                x = format(blob.classify())
                y = format(accuracy)
                employee_writer.writerow([listagem[2], x, y])
            except IndexError:
                x = 'null'      

RunAnalysis(dInfoMoney, 'naiveInfoMoney')
RunAnalysis(dInvesting, 'naiveInvesting')

# frase = 'Após um bom período de acumulação, VALE3 finalmente rompeu os 56,00 com um belíssimo candle de alta, fechando praticamente na máxima da semana aos 61,00.  O papel agora tem como alvo a região dos 67,00.'

# frase = 'Padrão de venda também em Bradesco. ALT. Bat. extremo das medidas oferecendo uma oportunidade de pouco risco e bastante retorno.'

# blob = TextBlob(frase,classifier=cl)

# print('Esta frase é de caráter:{}'.format(blob.classify()))
# print('Precisão da previsão:{}'.format(accuracy))

