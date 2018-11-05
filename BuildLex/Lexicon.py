import nltk 
from nltk import FreqDist
from collections import Counter

def RemoveStopWords(instancia):
    instancia  = instancia.lower()
    stopwords = set(nltk.corpus.stopwords.words('portuguese'))
    palavras = [i for i in instancia.split() if not i in stopwords]
    return (" ".join(palavras))

text = "Estou acreditando na retomada da CIEL3. Após perda do canal de alta, o ativo formou sexta-feira um duplo fundo e dá oportunidade de compra. Devo entrar a partir de amanhã com a superação da máxima de hoje."

texto = RemoveStopWords(text)

x = Counter(texto.split()).most_common()

print(texto)

# print(x)