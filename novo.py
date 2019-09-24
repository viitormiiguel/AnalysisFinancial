import pandas as pd
import csv 
import datetime 
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

Type_new = pd.Series([]) 
## Faz a leitura do arquivo
df = pd.read_csv('C:\\Users\\vitor\\Desktop\\dataset_novo.csv', delimiter=';') 
# mostra as 10 primeiras instancias do dataset
df['NOITE_DIA'] = df['NOITE_DIA'].apply(int)
novo = df.head(10)
## Dropa as variaveis que nao serao utilizadas
##X = novo.drop(columns=['ID','LONGITUDE','LATITUDE','LOG1','LOG2','PREDIAL1','LOCAL_VIA','QUEDA_ARR','DATA','DATA_HORA','FERIDOS','FERIDOS_GR','MORTE_POST','FATAIS','AUTO','TAXI','LOTACAO','ONIBUS_URB','ONIBUS_MET','ONIBUS_INT',
##'CAMINHAO','MOTO','CARROCA','BICICLETA','OUTRO','FONTE','BOLETIM','DIA','MES','ANO','FX_HORA','CONT_ACID','CONT_VIT','UPS','CONSORCIO','CORREDOR'])

print(df)