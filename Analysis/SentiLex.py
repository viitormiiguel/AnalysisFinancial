import nltk 
import csv 
import re 
import datetime 

now = datetime.datetime.now()
today = now.strftime("%Y-%m-%d")

sentilex = open("Lexicon/SentiLex/SentiLex-lem-PT01.txt", 'r', encoding="utf8")

dic_palavra = {}
for i in sentilex.readlines():
    pos_ponto = i.find('.')
    palavra = (i[:pos_ponto])
    pol_pos = i.find('POL')
    polaridade = (i[pol_pos+4:pol_pos+6]).replace(';','')
    dic_palavra[palavra] = polaridade
    
def Score_sentimento(frase):
    frase = frase.lower()
    l_sentimento = []
    for p in frase.split():
        l_sentimento.append(int(dic_palavra.get(p, 0)))
    score = sum(l_sentimento)
    if score > 0:
        return 'Positivo, Score:{}'.format(score)
    elif score == 0:
        return 'Neutro, Score:{}'.format(score)
    else:
        return 'Negativo, Score:{}'.format(score)

dInfoMoney = 'C:/Users/vitor/Documents/GetDataset/Infomoney/'
dInvesting = 'C:/Users/vitor/Documents/GetDataset/Investing.com/'
dTrading = 'C:/Users/vitor/Documents/GetDataset/TradingView/'

def RunAnalysis(fonte):
    # INFOMONEY
    with open(fonte + today +'/dataset.csv', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        dataInfo = [r for r in reader]
    with open(fonte + today +'/polaritySentilex.csv', mode='w', encoding="utf8") as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)    
        for lista2 in dataInfo:
            try:
                x = Score_sentimento(lista2[2])
                x = str(x)
                employee_writer.writerow([lista2[2], x])
            except IndexError:
                x = 'null'

RunAnalysis(dInfoMoney)
RunAnalysis(dInvesting)
RunAnalysis(dTrading)