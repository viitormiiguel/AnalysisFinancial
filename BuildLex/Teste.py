import nltk 

def get_index(in_list, in_string):
    for num, row in enumerate(in_list):
        if in_string in row:
            return num 

book = open('C:/Users/vitor/Documents/Python Projects/AnalysisFinancial/BuildLex/ebook.txt', 'r').read()

rows = book.split('\n')

start_idx = get_index(rows, ' START')
end_idx = get_index(rows, ' END')

rows = rows[start_idx + 1 : end_idx]

words = [s.lower().split() for s in rows if s]

words = [sublist for l in words for sublist in l]

stop = open('C:/Users/vitor/Documents/Python Projects/AnalysisFinancial/BuildLex/stop.txt', 'r').read() 

stop = stop.split('\n')

words = [''.join(c for c in w if c.isalpha()) for w in words]
words = [w for w in words if w not in stop and w.isalpha()]

text = nltk.Text(words)

freq = nltk.FreqDist(text)

freq.most_common(30)
freq.plot(30)