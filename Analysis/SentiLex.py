import nltk 
import csv 
import re 
import datetime 

now = datetime.datetime.now()
today = now.strftime("%Y-%m-%d")

stemmer = nltk.stem.RSLPStemmer()

sentilex = open("C:/Users/vitor/Documents/PythonProjects/AnalysisFinancial/Lexicon/SentiLex/SentiLex-lem-PT01.txt", 'r')

dic_palavra = {}
for i in sentilex.readlines():
    pos_ponto = i.find('.')
    palavra = (i[:pos_ponto])
    pol_pos = i.find('POL')
    polaridade = (i[pol_pos+4:pol_pos+6]).replace(';','')
    dic_palavra[palavra] = polaridade

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

def RunAnalysis(fonte, tipo, acao):
    with open(fonte + today +'/' + acao + '.csv') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        dataInfo = [r for r in reader]
        print(fonte + ':', len(dataInfo))
    with open(fonte + today +'/' + tipo + '_' + acao + '.csv', mode='w',  newline='') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=';', quoting=csv.QUOTE_MINIMAL)    
        for lista2 in dataInfo:
            try:
                # Contar apenas textos ja rotulados
                if lista2[1]:
                    if tipo == 'polaritySentiLexNo':
                        x = Score_sentimento_pre(lista2[2])
                        x = str(x)
                    else:
                        x = Score_sentimento(lista2[2])
                        x = str(x)
                    employee_writer.writerow([lista2[2], x])
            except IndexError:
                x = 'null'

# RunAnalysis(dInfoMoney, 'polaritySentiLexNo')
# RunAnalysis(dInvesting, 'polaritySentiLexNo')
# RunAnalysis(dTrading, 'polaritySentiLexNo')

# RunAnalysis(dInfoMoney, 'polaritySentiLexPre')
# RunAnalysis(dInvesting, 'polaritySentiLexPre')
RunAnalysis(dTrading, 'polaritySentiLexPre', 'petr4')
RunAnalysis(dTrading, 'polaritySentiLexPre', 'brfs3')
RunAnalysis(dTrading, 'polaritySentiLexPre', 'bbdc4')
RunAnalysis(dTrading, 'polaritySentiLexPre', 'ciel3')
RunAnalysis(dTrading, 'polaritySentiLexPre', 'goll4')
RunAnalysis(dTrading, 'polaritySentiLexPre', 'itsa4')
RunAnalysis(dTrading, 'polaritySentiLexPre', 'natu3')
RunAnalysis(dTrading, 'polaritySentiLexPre', 'abev3')