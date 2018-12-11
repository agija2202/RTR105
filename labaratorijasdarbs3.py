#Aptuveni novērtējot funkcijas saknes vertību lietojo "peli" iegūstam x =

from math import sinh,fabs
from time import sleep


def f(x):
    return sinh(x)

k = 0
a = -1
b = 1

from numpy import *
from matplotlib import pyplot as plt
x = linspace(0 , 4 , 70)
y = sinh(x)

plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Funkcija $sinh(x)$')
plt.plot(x, y, color = '#FF0000',linewidth = 5.0)
plt.show()

funa = f(a)
fnub = f(b)


if (funa*fnub >0.0):
    print('Dotajā intervālā [%s,%s] sakņu nav'%(a,b))
    sleep(1);exit()
else:
    print('Dotajā intervālā sakne(s) ir!')
deltax = 0.0001

while(fabs(b-a) > deltax):
    k = k+1
    x=(a+b)/2.;funx=f(x)
    print(a,b,x)
    if(funa*fnub < 0.):
        b = x
    else:
        a = x

print('Sakne ir: ',x)
print('Sakne ir: ',f(x))
print('Interāciju skaits k = ',k)

