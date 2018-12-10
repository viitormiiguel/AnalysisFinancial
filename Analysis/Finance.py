import nltk 
import csv 
import re 
import datetime 

now = datetime.datetime.now()
today = now.strftime("%Y-%m-%d")

dInfoMoney = 'C:/Users/vitor/Documents/GetDataset/Infomoney/'
dInvesting = 'C:/Users/vitor/Documents/GetDataset/Investing.com/'
dTrading = 'C:/Users/vitor/Documents/GetDataset/TradingView/'

stemmer = nltk.stem.RSLPStemmer()

finance = open(dTrading + today + "/lexicon-tf-idf-1.txt", 'r', encoding="utf8")

dic_palavra = {}
for i in finance.readlines():
    pos_ponto = i.find(',')
    palavra = (i[:pos_ponto])
    pol_pos = (i[pos_ponto+1:pos_ponto+4])
    dic_palavra[palavra] = pos_ponto

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

def RunAnalysis(fonte, tipo):
    with open(fonte + today +'/dataset.csv', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        dataInfo = [r for r in reader]
    with open(fonte + today +'/' + tipo + '.csv', mode='w', encoding="utf8") as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)    
        for lista2 in dataInfo:
            try:
                # Contar apenas textos ja rotulados
                if not lista2[1]:
                    if tipo == 'polarityFinanceNo':
                        x = Score_sentimento_pre(lista2[2])
                        x = str(x)
                    else:
                        x = Score_sentimento(lista2[2])
                        x = str(x)
                    employee_writer.writerow([lista2[2], x])
            except IndexError:
                x = 'null'

# RunAnalysis(dInfoMoney, 'polarityFinanceNo')
# RunAnalysis(dInvesting, 'polarityFinanceNo')
# RunAnalysis(dTrading, 'polarityFinanceNo')

# RunAnalysis(dInfoMoney, 'polarityFinancePre')
# RunAnalysis(dInvesting, 'polarityFinancePre')
RunAnalysis(dTrading, 'polarityFinancePre')