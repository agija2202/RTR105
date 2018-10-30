#-*- coding: utf-8 -*-
from math import sin
x=float(input("Lietotaj, lūdzu, ievadi argumentu (x)"))

y=sin(x)
print("sin(%.2f)= %6.2f"%(x,y))

a=(-1)**0*x**1/(1)
S= a
print ("a0 = %6.2f S=%.2f"%(a,S))

a=a*(-1)*x*x/(2*3)

S=S + a
print("al=%6.2f S=%6.2f"%(a,S))

a=a*(-1)*x*x/(4*5)

S=S+a
print("a2=%6.2f S=%6.2f"%(a,S))

a =(-1)**3*x**7/(1*2*3*4*5*6*7)

S=S+a
print ("a3=%6.2f S=%6.2f"%(a,S))

a=a*(-1)*x*x/(6*7)
S= S+a
print ("a3=%6.2f S=%6.2f"%(a,S))
