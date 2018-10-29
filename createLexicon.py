import nltk
import csv
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import imp

now = datetime.datetime.now()
today = now.strftime("%Y-%m-%d")

dTrading = 'C:/Users/vitor/Documents/GetDataset/TradingView/'

def RunFile(fonte, tipo):
    with open(fonte + today +'/dataset.csv', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        dataInfo = [r for r in reader]
        datasetP = []
        datasetN = []
        for dados_tests in dataInfo:
            try: 
                if 'Alta' in dados_tests[1]:
                    x = dados_tests[1]
                    y = dados_tests[2]
                    dinside = (y, x)
                    datasetP.append(dinside)
                if 'Baixa' in dados_tests[1]:
                    x = dados_tests[1]
                    y = dados_tests[2]
                    dinside = (y, x)
                    datasetN.append(dinside)
            except IndexError:
                x = 'null'

RunFile(dTrading, 'lexiconFinance')