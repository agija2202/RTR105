'''
from numpy import *
x = linspace(0,7,70)
y = cos(x)
from matplotlib import pyplot as plt
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Funkcija $cos(x)$')
plt.plot(x,y)
plt.show() 
plt.plot(x,y,color = "#FF0000")
'''
'''
from numpy import *
x = linspace(0,7,70)
y2 = sin(x)
 
from matplotlib import pyplot as plt
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Funkcija $sin(x)$')
plt.plot(x,y2)
plt.plot(x,y2,color = "#FF33FF")
plt.show()
'''
from numpy import *
import matplotlib.pyplot as plt
x = linspace(0,4,70)
y = sin(x)
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title ('Funkcija $cos(x)$')
plt.plot(x,y,color = "#FF99FF",linewidth=2.0)

y1 = x
plt.plot(x,y1,color = "#FF0000",linewidth=2.0)
#y2 = x - x*x*x/(1*2*3)
y2 = y1 - x*x*x/ (1*2*3)
plt.plot(x, y2, color ="#0000FF")
#y3= x - x*x*x/(1*2*3) + x*x*x*x*x/(1*2*3*4*5)
y3 = y2 + x*x*x*x*x/ (1*2*3*4*5)
plt.plot(x,y3, color = "#FF00FF", linewidth=2.0)
plt.show()
