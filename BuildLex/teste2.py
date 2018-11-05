import sys 
import codecs
import nltk
from nltk.corpus import stopwords

now = datetime.datetime.now()
today = now.strftime("%Y-%m-%d")

dTrading = 'C:/Users/vitor/Documents/GetDataset/TradingView/'

default_stopwords = set(nltk.corpus.stopwords.words('portuguese'))

input_file = "C:/Users/vitor/Documents/GetDataset/TradingView/2018-04-11/dataset.csv"

def divideDataset(fonte, tipo):
    with open(fonte + today + '/dataset.csv', encoding="utf8") as datacompare:
        reader = csv.reader(datacompare)
        next(reader)
        dados2 = [t for t in reader]