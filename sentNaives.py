import nltk 
import re 
import pandas as pd 
import csv
import datetime
import importlib

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics 
from sklearn.model_selection import cross_val_predict

now = datetime.datetime.now()
today = now.strftime("%Y-%m-%d")

dTrading = 'C:/Users/vitor/Documents/GetDataset/TradingView/'

dataset = pd.read_csv(dTrading + today + '/dataset.csv')

textos = dataset['Text'].values
classes = dataset['Class'].values

vectorizer = CountVectorizer(analyzer="word")
freq_textos = vectorizer.fit_transform(textos)
modelo = MultinomialNB()
modelo.fit(freq_textos,classes)

testes = ["No gráfico semanal e diário ABEV3 vem respeitando esse canal de alta. Minha expectativa é de buscar os R$23 até o fim do ano.",
"BTCUSD rompeu acunha descendente o que abre possibilidade de padrão altista",
"GGBR4 atingiu a correção de sua perna de alta, objetivo de FIBO (retração de ouro, 61.8%) a qual corresponde também a um suporte horizontal (um fundo anterior)."]

# freq_textos = vectorizer.transform(testes)
# modelo.predict(freq_textos)