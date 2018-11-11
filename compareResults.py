import csv
import re 
import importlib 
import datetime 
import imp

now = datetime.datetime.now()
today = now.strftime("%Y-%m-%d")

dTrading = 'C:/Users/vitor/Documents/GetDataset/TradingView/'

def RunCompare(fonte, tipo):
    # countPos = 0 
    # countNeg = 0
    # countNeu = 0
    # lexPos = 0
    # lexNeg = 0
    # lexNeu = 0
    # ARQUIVO GERADO PELO LEXICO
    with open(fonte + today +'/' + tipo + '.csv', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        dados1 = [r for r in reader]
        # print(dados1[1][0])
    # DATASET COLETADO JA ROTULADO
    with open(fonte + today + '/dataset.csv', encoding="utf8") as datacompare:
        reader = csv.reader(datacompare)
        next(reader)
        dados2 = [t for t in reader]
        # print(dados2[2][2])
        with open (fonte + today + '/compare.csv', mode='w', encoding='utf8') as new_file:
            new_file = csv.writer(new_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for v1 in dados2:
                try:
                    if v1[1]:
                        new_file.writerow([v1[2], v1[1]])
                except IndexError:
                    x = 'null'            
            

RunCompare(dTrading, 'polaritySentiLexPre')

# def Teste(fonte, tipo):
#     with open(fonte + today +'/' + tipo + '.csv', encoding="utf8") as d1:
#         with open(fonte + today + '/dataset.csv', encoding="utf8") as d2:
#             same = set(d1).intersection(d2)
#     same.discard('\n')
#     with open(fonte + today + 'teste.csv')

# Teste(dTrading,'polaritySentiLexPre')

# for valores in dados2:
        #     try:
        #         if valores[1]:
        #             x = 'Teste'
        #             if valores[1] == 'Viés de alta':
        #                 valores[1] = valores[1].replace('Viés de alta','Positivo')
        #                 countPos += 1
        #             if valores[1] == 'Viés de baixa':
        #                 valores[1] = valores[1].replace('Viés de baixa','Negativo')
        #                 countNeg += 1
        #             if valores[1] == 'Educação':
        #                 valores[1] = valores[1].replace('Educação','Neutro')
        #                 countNeu += 1
        #     except IndexError:
        #         x = 'null'
        # for valores2 in dados1:
        #     try:
        #         if valores2[1]:
        #             x = 'Teste' 
        #             if 'Positivo' in valores2[1]:
        #                 lexPos += 1
        #             if 'Negativo' in valores2[1]:
        #                 lexNeg += 1
        #             if 'Neutro' in valores2[1]:
        #                 lexNeu += 1
        #     except IndexError:
        #         x = 'null'
        # print("Positivos: ", countPos)
        # print("Negativos: ", countNeg)
        # print("Neutros: ", countNeu)
        # print("Lex Positivos: ", lexPos)
        # print('Lex Negativos: ', lexNeg)
        # print('Lex Neutros: ', lexNeu)    