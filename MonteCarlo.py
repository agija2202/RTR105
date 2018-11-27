#coding : utf-8                                                            (valodas maiņa)
#1. N vienmērīgi sadalīti skaitļi
# N uniform devided numbers

import sys                                                                 (sinus funkcija)
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')

from numpy import random 

#pseido-gadījumu skaitļu ģenerātora grauds
# random.seed(1)

N = 10000                                                                  (punktu skaits grafikā)

x = random.uniform(0,5,N)
'''
#x = random.normal(2.5,5,N)                      (Iegūstam grafiku ar noteikto punktu(N) skaitu līdz ar to visi punkti ir viena krāsā un noteikt skaits ir attelots grafikā)
k = [0,0,0,0,0]
for i in range (N) :
    if x[i] < 1:
        k[0] = k[0] + 1
    elif x[i] < 2:
        k[1] = k[1] + 1
    elif x[i] < 3:
        k[2] = k[2] + 1
    elif x[i] < 4:
        k[3] = k[3] + 1
    else:
        k[4] = k[4] + 1
print(k)
print(sum(k))
'''
(Iegustam punktu skaitu un sadalām to krāsu uz pusēm, sarkano un zaļo) 
y = random.uniform(0,5,N)
N1 = 0
from matplotlib import pyplot as plt
plt.grid()
for i in range(N):
    #plt.plot(x[i],y[i],'ko')
    if x[i] > 0 and x[i] < 5:
        if y[i] > 0 and y[i] < x[i]:
            plt.plot(x[i],y[i],'go')
            N1 = N1 + 1
        else:
            plt.plot(x[i],y[i],'ro')
plt.show()
(Parādās grafiks ar pun kitu skaitu un tad aizverot to mēs redezam ieguto skaitli kuram ir jābūt apmēram 12,5 )

S_zinaamais = 5 * 5
S_nezinaamais = 1. * S_zinaamais * N1/N
print(S_nezinaamais)
plt.show()
