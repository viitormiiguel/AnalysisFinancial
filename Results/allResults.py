import numpy as np
import matplotlib.pyplot as plt

N = 3
pos = (20, 35, 30)
neu = (25, 32, 34)
neg = (0 , 0 , 0)
menStd = (2, 3, 4,)
womenStd = (3, 5, 2)
ind = np.arange(N)    # the x locations for the groups
width = 0.45       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, pos, width, yerr=menStd)
p2 = plt.bar(ind, neu, width, yerr=menStd)
p3 = plt.bar(ind, neg, width,
             bottom=pos, yerr=womenStd)

plt.ylabel('Scores')
plt.title('Scores by group and gender')
plt.xticks(ind, ('G1', 'G2', 'G3'))
plt.yticks(np.arange(0, 81, 10))
plt.legend((p1[0], p2[0]), ('Pos', 'Neu', 'Neg'))

plt.show()