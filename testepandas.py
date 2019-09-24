import pandas as pd
import csv 
import datetime 

Type_new = pd.Series([]) 
## Faz a leitura do arquivo
df = pd.read_csv('C:\\Users\\vitor\\Desktop\\acidentes-2016.csv', delimiter=';') 
# mostra as 10 primeiras instancias do dataset
# novo = df.head(10)
novo = df
## Dropa as variaveis que nao serao utilizadas
X = novo.drop(columns=['ID','LONGITUDE','LATITUDE','LOG1','LOG2','PREDIAL1','LOCAL_VIA','QUEDA_ARR','DATA','DATA_HORA','FERIDOS','FERIDOS_GR','MORTE_POST','FATAIS','AUTO','TAXI','LOTACAO','ONIBUS_URB','ONIBUS_MET','ONIBUS_INT',
'CAMINHAO','MOTO','CARROCA','BICICLETA','OUTRO','FONTE','BOLETIM','DIA','MES','ANO','FX_HORA','CONT_ACID','CONT_VIT','UPS','CONSORCIO','CORREDOR'])

def is_between(time, time_range):
    if time_range[1] < time_range[0]:
        return time >= time_range[0] or time <= time_range[1]
    return time_range[0] <= time <= time_range[1]


with open('C:\\Users\\vitor\\Desktop\\dataset_novo.csv', 'w', newline='') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=';', quoting=csv.QUOTE_MINIMAL)
    employee_writer.writerow(['LOCAL', 'TIPO_ACID', 'DIA_SEM', 'HORA_PICO', 'MORTES', 'TEMPO', 'NOITE_DIA', 'REGIAO'])
    for index, row in X.iterrows():

        if row['LOCAL'] == 'Cruzamento':
            row['LOCAL'] = '1'
        elif row['LOCAL'] == 'Logradouro':
            row['LOCAL'] = '2'

        if row['TIPO_ACID'] == 'ABAROLAMENTO':
            row['TIPO_ACID'] = '1'
        elif row['TIPO_ACID'] == 'ATROPELAMENTO':
            row['TIPO_ACID'] = '2'
        elif row['TIPO_ACID'] == 'CHOQUE':
            row['TIPO_ACID'] = '3'
        elif row['TIPO_ACID'] == 'COLISAO':
            row['TIPO_ACID'] = '4'
        elif row['TIPO_ACID'] == 'CAPOTAGEM':
            row['TIPO_ACID'] = '5'
        elif row['TIPO_ACID'] == 'EVENTUAL':
            row['TIPO_ACID'] = '6'
        elif row['TIPO_ACID'] == 'INCENDIO':
            row['TIPO_ACID'] = '7'
        elif row['TIPO_ACID'] == 'QUEDA':
            row['TIPO_ACID'] = '8'
        else:
            row['TIPO_ACID'] = '9'

        if row['DIA_SEM'] == 'SABADO':
            row['DIA_SEM'] = '1'
        elif row['DIA_SEM'] == 'DOMINGO':
            row['DIA_SEM'] = '2'
        elif row['DIA_SEM'] == 'SEGUNDA-FEIRA':
            row['DIA_SEM'] = '3'
        elif row['DIA_SEM'] == 'TERCA-FEIRA':
            row['DIA_SEM'] = '4'
        elif row['DIA_SEM'] == 'QUARTA-FEIRA':
            row['DIA_SEM'] = '5'
        elif row['DIA_SEM'] == 'QUINTA-FEIRA':
            row['DIA_SEM'] = '6'
        else:
            row['DIA_SEM'] = '7'
        
        if row['REGIAO'] == 'SUL':
            row['REGIAO'] = '1'
        elif row['REGIAO'] == 'NORTE':
            row['REGIAO'] = '2'
        elif row['REGIAO'] == 'LESTE':
            row['REGIAO'] = '3'
        else:
            row['REGIAO'] = '4'

        if row['TEMPO'] == 'BOM':
            row['TEMPO'] = '1'
        elif row['TEMPO'] == 'CHUVOSO':
            row['TEMPO'] = '2'
        else:
            row['TEMPO'] = '3'

        if row['NOITE_DIA'] == 'DIA':
            row['NOITE_DIA'] = '1'
        elif row['NOITE_DIA'] == 'NOITE':
            row['NOITE_DIA'] = '2'

        if row['HORA'] != ' ':
            if is_between(str(row['HORA']), ("07:30", "09:00")) == True or is_between(str(row['HORA']), ("17:00","19:00")) == True:
                row['HORA'] = 1
            else:
                row['HORA']  = 0
        else:
            row['HORA']  = 0

        employee_writer.writerow([row['LOCAL'], row['TIPO_ACID'], row['DIA_SEM'], row['HORA'], row['MORTES'], row['TEMPO'], str(row['NOITE_DIA']), row['REGIAO']])
        # break

X.insert(8, "HORARIO PICO", Type_new)

# print(X)
