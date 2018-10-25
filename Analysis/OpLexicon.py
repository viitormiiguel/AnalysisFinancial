import nltk 
import csv 
import re 
import datetime 

now = datetime.datetime.now()
today = now.strftime("%Y-%m-%d")

oplexicon = open('Lexicon/OpLexicon/lexico_v2.txt', 'r', encoding="utf8") 

dic_palavra = {}
for i in oplexicon.readlines():
    pos_ponto = i.find(',')
    palavra = (i[:pos_ponto])
    pol_pos = re.findall(r'-?\d+\.?\d*', str(i))
    if pol_pos:
        polaridade = pol_pos[0]
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
    with open(fonte + today +'/dataset.csv', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        dataInfomoney = [r for r in reader]
    with open(fonte + today +'/polarityOpLexicon.csv', mode='w', encoding="utf8") as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)    
        for lista2 in dataInfomoney:
            try:
                x = Score_sentimento(lista2[2])
                x = str(x)
                employee_writer.writerow([lista2[2], x])
            except IndexError:
                x = 'null'

RunAnalysis(dInfoMoney)
RunAnalysis(dInvesting)
RunAnalysis(dTrading)