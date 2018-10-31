import csv
import re 
import importlib 
import datetime 

now = datetime.datetime.now()
today = now.strftime("%Y-%m-%d")

dTrading = 'C:/Users/vitor/Documents/GetDataset/TradingView/'

def RunCompare(fonte, tipo):
    countPos = 0 
    countNeg = 0
    countNeu = 0
    lexPos = 0
    lexNeg = 0
    lexNeu = 0
    # ARQUIVO GERADO PELO LEXICO
    with open(fonte + today +'/' + tipo + '.csv', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        dados1 = [r for r in reader]
    # DATASET COLETADO JA ROTULADO
    with open(fonte + today + '/dataset.csv', encoding="utf8") as datacompare:
        reader = csv.reader(datacompare)
        next(reader)
        dados2 = [t for t in reader]
        for valores in dados2: 
            for valores2 in dados1:
                try:
                    if valores[1]:
                        x = "Teste"
                        if valores[1] == 'Viés de alta':
                            valores[1] = valores[1].replace('Viés de alta','Positivo')
                            countPos += 1
                        if valores[1] == 'Viés de baixa':
                            valores[1] = valores[1].replace('Viés de baixa','Negativo')
                            countNeg += 1
                        if valores[1] == 'Educação':
                            valores[1] = valores[1].replace('Educação','Neutro')
                            countNeu += 1
                        if 'Positivo' in valores[1]: 
                            if 'Positivo' in valores2[1]:
                                lexPos += 1
                        if 'Negativo' in valores[1]: 
                            if 'Negativo' in valores2[1]:
                                lexNeg += 1
                        if 'Neutro' in valores[1]: 
                            if 'Neutro' in valores2[1]:
                                lexNeu += 1
                except IndexError:
                    x = 'null'
        print("Positivos: ", countPos)
        print("Lex Positivos: ", lexPos)
        print("Negativos: ", countNeg)
        print('Lex Negativos: ', lexNeg)
        print("Neutros: ", countNeu)
        print('Lex Neutros: ', lexNeu)

RunCompare(dTrading, 'polaritySentiLexPre')