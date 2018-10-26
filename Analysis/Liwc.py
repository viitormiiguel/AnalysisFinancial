import nltk 
import csv 
import re 
import datetime 
import itertools

now = datetime.datetime.now()
today = now.strftime("%Y-%m-%d")

stemmer = nltk.stem.RSLPStemmer()

liwc = open('Lexicon/Liwc/liwc_pt.txt', 'r')
count = 0
for line in liwc.readlines(): count += 1

dic_palavra = {}
liwc = open('Lexicon/Liwc/liwc_pt.txt', 'r')
pol = {}
for line in itertools.islice(liwc, 67, count):
    pos_ponto = line.replace('\\t',',')
    p1 = pos_ponto.find(',')
    palavra = (line[:p1])
    polar = line[p1:].replace('\\t',',')
    if '127' in polar:
        polar = '-1'
    else: 
        if '126' in polar:
            polar = '1'
        polar = '0'
    dic_palavra[palavra] = polar

def RemoveStopWords(instancia):
    instancia  = instancia.lower()
    stopwords = set(nltk.corpus.stopwords.words('portuguese'))
    palavras = [i for i in instancia.split() if not i in stopwords]
    return (" ".join(palavras))
    
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

def Score_sentimento_pre(frase):
    # Conversao para minusculos
    frase = frase.lower()
    # Remoção de numeros
    frase = re.sub('[-10-9]','', frase)
    # Remoçao de pontuação
    frase = re.sub(r'[-./?!,":;()\']','',frase)
    # Remoção de stopwords
    texto = RemoveStopWords(frase)
    l_sentimento = []
    for p in texto.split():
        # Stemming 
        l_sentimento.append(int(dic_palavra.get(stemmer.stem(p), 0)))
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

def RunAnalysis(fonte, tipo):
    with open(fonte + today +'/dataset.csv', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        dataInfo = [r for r in reader]
    with open(fonte + today +'/' + tipo + '.csv', mode='w', encoding="utf8") as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)    
        for lista2 in dataInfo:
            try:
                if tipo == 'polarityLiwcNo':
                    x = Score_sentimento_pre(lista2[2])
                    x = str(x)
                else: 
                    x = Score_sentimento(lista2[2])
                    x = str(x)
                employee_writer.writerow([lista2[2], x])
            except IndexError:
                x = 'null'

RunAnalysis(dInfoMoney, 'polarityLiwcNo')
RunAnalysis(dInvesting, 'polarityLiwcNo')
RunAnalysis(dTrading, 'polarityLiwcNo')

RunAnalysis(dInfoMoney, 'polarityLiwcPre')
RunAnalysis(dInvesting, 'polarityLiwcPre')
RunAnalysis(dTrading, 'polarityLiwcPre')