import nltk
import csv
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

now = datetime.datetime.now()
today = now.strftime("%Y-%m-%d")

dInfoMoney = 'C:/Users/vitor/Documents/GetDataset/Infomoney/'
dInvesting = 'C:/Users/vitor/Documents/GetDataset/Investing.com/'
dTrading = 'C:/Users/vitor/Documents/GetDataset/TradingView/'

# Resultados Investing.com
r_investing = open(dInvesting + today +'/polarityOpLexiconPre.csv', 'r', encoding='utf8')
# r_investing = open(dInvesting + today +'/polarityOpLexiconNo.csv', 'r', encoding='utf8')
posInv = 0 
neuInv = 0 
negInv = 0
for t in r_investing.readlines():
    if 'Positivo' in t:
        posInv += 1
    if 'Neutro' in t:
        neuInv += 1
    if 'Negativo' in t:
        negInv += 1
print('Investing Pos ', posInv)
print('Investing Neu ', neuInv)
print('Investing Neg ', negInv)

# Resultados InfoMoney
r_infomoney = open(dInfoMoney + today +'/polarityOpLexiconPre.csv', 'r', encoding='utf8')
# r_infomoney = open(dInfoMoney + today +'/polarityOpLexiconNo.csv', 'r', encoding='utf8')
posInf = 0
neuInf = 0 
negInf = 0
for t in r_infomoney.readlines():
    if 'Positivo' in t:
        posInf += 1
    if 'Neutro' in t:
        neuInf += 1
    if 'Negativo' in t:
        negInf += 1
print('InfoMoney Pos ', posInf)
print('InfoMoney Neu ', neuInf)
print('InfoMoney Neg ', negInf)

# Resultados TradingView
r_tradingview = open(dTrading + today +'/polarityOpLexiconPre.csv', 'r', encoding='utf8')
# r_tradingview = open(dTrading + today +'/polarityOpLexiconNo.csv', 'r', encoding='utf8')
posTrd = 0
neuTrd = 0 
negTrd = 0
for t in r_tradingview.readlines():
    if 'Positivo' in t:
        posTrd += 1
    if 'Neutro' in t:
        neuTrd += 1
    if 'Negativo' in t:
        negTrd += 1
print('TradingView Pos ', posTrd)
print('TradingView Neu ', neuTrd)
print('TradingView Neg ', negTrd)

# raw_data = {'Fonte de Dados': ['Investing.com', 'InfoMoney', 'TradingView'],
#         'Pos': [posInv, posInf, posTrd],
#         'Neu': [neuInv, neuInf, neuTrd],
#         'Neg': [negInv, negInf, negTrd]}
# df = pd.DataFrame(raw_data, columns = ['Fonte de Dados', 'Pos', 'Neu', 'Neg'])
# df

# # Setting the positions and width for the bars
# pos = list(range(len(df['Pos']))) 
# width = 0.25 
# fig, ax = plt.subplots(figsize=(10,5))

# # Create a bar with pre_score data, # in position pos,
# plt.bar(pos, df['Pos'], width, alpha=0.5, color='#EE3224', label=df['Fonte de Dados'][0]) 

# # Create a bar with mid_score data, # in position pos + some width buffer,
# plt.bar([p + width for p in pos], df['Neu'], width, alpha=0.5, color='#F78F1E', label=df['Fonte de Dados'][1]) 

# # Create a bar with post_score data, # in position pos + some width buffer,
# plt.bar([p + width*2 for p in pos], df['Neg'], width, alpha=0.5, color='#FFC222', label=df['Fonte de Dados'][2]) 

# ax.set_title("OpLexicon sem Pré-Processamento")
# ax.set_ylabel('N° de Textos')
# ax.set_xticks([p + 1 * width for p in pos])
# ax.set_xticklabels(df['Fonte de Dados'])

# plt.xlim(min(pos)-width, max(pos)+width*4)
# plt.ylim([0, max(df['Pos'] + df['Neu'] + df['Neg'])] )

# plt.legend(['Positivo', 'Neutro', 'Negativo'], loc='upper left')
# plt.grid()
# plt.show()