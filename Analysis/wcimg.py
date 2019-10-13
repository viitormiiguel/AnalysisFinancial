from os import path, getcwd
from PIL import Image 
import numpy as np 
import matplotlib.pyplot as plt 
from wordcloud import WordCloud, ImageColorGenerator
import datetime

now = datetime.datetime.now()
today = now.strftime("%Y-%m-%d")

dTrading = 'C:/Users/vitor/Documents/GetDataset/TradingView/'

def runWord(ativo, imagem, pol):
    d = getcwd()

    text = ""
    with open(dTrading + today + '/words-' + ativo + '.txt', 'r', encoding="utf8") as fp:
        line = fp.readline()
        while line:
            s = line.split('-')
            if pol in s[0]:
                text += " " + s[1]
            line = fp.readline()
        fp.close()

    mask = np.array(Image.open(path.join(d, "img/" + imagem)))
    wc = WordCloud(background_color="white", max_words=50, mask=mask, max_font_size=90, random_state=42)

    wc.generate(text)

    image_colors = ImageColorGenerator(mask)
    plt.figure(figsize=[4,4])
    plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
    plt.axis("off")
    plt.savefig('C:/xampp/htdocs/SaMaWeb/public/img/wordcloud/' + ativo + '_' + pol + '.png')
    plt.savefig('Analysis/wc/' + ativo + '_' + pol + '.png')
    # plt.show()

# runWord('petr4')
# runWord('brfs3')
# runWord('bbdc4')
# runWord('ciel3')
# runWord('goll4', 'goll.png', 'p')
# runWord('goll4', 'goll.png', 'n')
# runWord('itsa4', 'itau.jpg', 'p')
# runWord('itsa4', 'itau.jpg', 'n')
# runWord('natu3', 'natura.png', 'p')
# runWord('natu3', 'natura.png', 'n')
# runWord('petr4', 'petrobras.png', 'p')
# runWord('petr4', 'petrobras.png', 'n')

# runWord('abev3')