# -*-   coding: utf-8 -*-
from math import *
x = float (input("Lietotāj , lūdzu . idavadi argumentu (x): "))

print("x = %.2f sin(x) = %.2f"%(x,sin(x)))

y = sin(x)
print("             500")
print("          ---------")
print("          \\                       2*k+1")
print ("           \\                    k ")
print ("sin(x) = |            -------------------------")
print ("           /                     (2*k+1)! ")
print("          /")
print("          ---------")
print("           k = 0")


                             
print("rekurences reizinatajs:   --------------------------")
print("sin(%.2f) = %.2f"%(x,y))
a0 = (x)**1/(1)
S0 = a0
print("a0 = %.2f S0 = %.2f"%(a0,S0))

a1 = (x)**3/(1*2*3)
S1 = a0 + a1
print("a1 = %.2f S1 = %.2f"%(a1,S1))

a2 = (x)**5/(1*2*3*4*5)
S2 = a0 + a1 + a2
print("a2 = %.2f S2 = %.2f"%(a2,S2))

a3 = (x)**7/(1*2*3*4*5*6*7)
S3 = a0 + a1 + a2 + a3
print("a3 = %.2f S3 = %.2f"%(a3,S3))


x = float (input("Lietotāj , lūdzu , ievadi argumentu (x): "))
y = sin(x)

print("sin(%.2f) = %.2f"%(x,y))
a0 = (x)**1/(1)
S = a0
print("a0 = %.2f S0 = %.2f"%(a0,S0))

S = S + a1
print("a1 = %.2f S1 = %.2f"%(a1,S))

a2 = (x)**5/(1*2*3*4*5)
S = S + a2
print("a2 = %.2f S2 = %.2f"%(a2,S))

a3 = (x)**7/(1*2*3*4*5*6*7)
S3 = S + a3
print("a3 = %.2f S3 = %.2f"%(a3,S))


            
