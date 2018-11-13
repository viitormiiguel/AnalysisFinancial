import csv
import re  
import datetime 

now = datetime.datetime.now()
today = now.strftime("%Y-%m-%d")

dTrading = 'C:/Users/vitor/Documents/GetDataset/TradingView/'

def RunCompare(fonte):
    # DATASET COLETADO JA ROTULADO
    neutro = 0
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
                        if v1[1] == 'Viés de alta':
                            v1[1] = v1[1].replace('Viés de alta','Positivo')
                        if v1[1] == 'Viés de baixa':
                            v1[1] = v1[1].replace('Viés de baixa','Negativo')
                        if v1[1] == 'Educação':
                            v1[1] = v1[1].replace('Educação','Neutro')
                            neutro += 1
                        new_file.writerow([v1[2], v1[1]])
                except IndexError:
                    _ = 'null'
        print("Neutros ", neutro)

RunCompare(dTrading)

def Comparation(a1, a2):
    f1 = open(a1, encoding="utf8")
    f2 = open(a2, encoding="utf8")

    f1_line = f1.readline()
    f2_line = f2.readline()
    line_no = 1

    pospos = 0
    posneg = 0
    posneu = 0
    negneg = 0
    negpos = 0
    negneu = 0
    neuneu = 0
    neuneg = 0
    neupos = 0

    while f1_line != '' or f2_line != '':
        f1_line = f1_line.rstrip()
        f2_line = f2_line.rstrip()
        
        if f1_line != f2_line:
            if 'Negativo' in f2_line:
                if 'Negativo' in f1_line:
                    negneg += 1
                if 'Positivo' in f1_line:
                    negpos += 1
                if 'Neutro' in f1_line:
                    negneu += 1
            if 'Positivo' in f2_line:
                if 'Negativo' in f1_line:
                    posneg += 1
                if 'Positivo' in f1_line:
                    pospos += 1
                if 'Neutro' in f1_line:
                    posneu += 1
            if 'Neutro' in f2_line:
                if 'Negativo' in f1_line:
                    neuneg += 1
                if 'Positivo' in f1_line:
                    neupos += 1
                if 'Neutro' in f1_line:
                    neuneu += 1

        #Read the next line from the file
        f1_line = f1.readline()
        f2_line = f2.readline()

        #Increment line counter
        line_no += 1
    
    print('Positivo pos: ', pospos)
    print('Positivo neu: ', posneu)
    print('Positivo neg: ', posneg)

    print('Neutro pos: ', neupos)
    print('Neutro neu: ', neuneu)
    print('Neutro neg: ', neuneg)

    print('Negativo pos: ', negpos)
    print('Negativo neu: ', negneu)
    print('Negativo neg: ', negneg)

    f1.close()
    f2.close()

Comparation(dTrading + today + '/compare.csv', dTrading + today + '/polaritySentiLexPre.csv')
# Comparation(dTrading + today + '/compare.csv', dTrading + today + '/polarityOpLexiconPre.csv')
# Comparation(dTrading + today + '/compare.csv', dTrading + today + '/polarityLiwcPre.csv')
