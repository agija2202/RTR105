#!/usr/bin/env python
# coding: utf-8

# In[1]:


#2. labors
#Ielādējam savu repozitāriju terminālā un islēdzam  idle & vidi kur sākam veidot funkciju

import sys
sys.path.append('ūser/local/anaconda3/lib/python3.6/site-packages')

# sys importē iebūvēto moduli (bibliotēku), kas nosaukts sys.

from numpy import sinh , linspace

#Sākumā ar linspace mēs noskām grafisko punku lauku kurā tie tiks iezīmēti manā gadijumā tā ie hiperboliska funkcija , līdz ar to tiek ievadītas tādas x vērtības bet y mēs ievadām formulas , lai gala rezultātā mēs iegutu vairākus grafikus vienā bildē.

x = linspace(0, 7, 70)
y = sinh(x)
y1 = x
y2 = y1 - x**3/(1*2*3)
y3 = y2 - x**5/(1*2*3*4*5)
y4 = y3 - x**7/(1*2*3*4*5*6*7)

#Ierakstām funkcijas kuras dos mums rezultātā funkcijas uz grafika  


from matplotlib import pyplot as plt

#Šī komanda ir zīmēšanas ietvars. Šī konkrētā importa līnija tikai importē moduli "matplotlib.pyplot" un piesaista to nosaukumam "plt", kā šis imports ietekmē funkcijas laukumu.

plt.grid()
plt.title('Funkcija $sinh(x)$')
plt.xlabel('f(x)')
plt.plot(x,y,color='#FF0098')
plt.plot(x,y1,color='#00FF11')
plt.plot(x,y2,color='#0000FF')
plt.plot(x,y3,color='#FFFF00')
plt.plot(x,y4,color='#00FFFF')

#Ar šīm komandām mēs piešķiram katram iepriekš ievadītajam funkcijas grafikam dažādas krāsas lai tā nesaplūstu kopā.

plt.legend(['sinh(x)', 'x', 'x-x**/(1*2*3)', 'x-x**5/(1*2*3*4*5)','x-x**7/(1*2*3*4*5*6*7)'], loc=3)

#Akcentējam to ka uz viena grafika gribam redzēt vairākas funkcijas 

plt.show()

#Parādā gala rezultātu komanda ar kuru pieprasām parādīt rezultātu


# In[ ]:




