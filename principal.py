# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 12:17:39 2020

@author: pablo

PROBLEMA 1 - 05/03/2020
you are organizing a Hash Code hub and want to order pizza for your hub’s

participants. Luckily, there is a nearby pizzeria with really good pizza.

The pizzeria has different types of pizza, and to keep the food offering for your hub

interesting, you can only order at most one pizza of each type. Fortunately, there are

many types of pizza to choose from!

Each type of pizza has a specified size: the size is the number of slices in a pizza of this

type.

You estimated the maximum number of pizza slices that you want to order for your

hub based on the number of registered participants. In order to reduce food waste,

your goal is to order as many pizza slices as possible, but not more than the
    
maximum number .

Para este problema existirán 3 entradas que condicionarán vuestro problema, y que inicialmente debereis generar para probar, y que yo variaré para comprobar la validez de la solución.
Un entero M: M<10^9. El número máximo de slices de pizza.
Un entero N: N<10^6 El número máximo de diferentes tipos de pizza
Una lista S, de longitud N, que contenga el número de trozos en cada tipo de pizza, en orden ascendente.

Ejemplo
M = 17
N = 4
S = [2 5 6 8]

Vuestra solución deberá estar compuesta por:

Un entero K: Número de tipos de pizza que necesitais (0 <= K <= N)
Una lista L de longitud K, indicando el tipo de pizza seleccionada.

En el caso anterior, si quereis 3 pizzas de 2,6 y 8 trozos cada una, vuestra solución será:
K = 3
L = [0 2 3]

"""
def decimalToBinary(n,ref):
    binary=bin(n).replace("0b","")
    refbin=bin(ref).replace("0b","")
    
    if len(binary)<len(refbin):         ##PARA NORMALIZAR EL TAMAÑO DEL STRING
        u=len(refbin)-len(binary)
        for i in range(u):
            binary='0'+binary
    return binary

def orden(lista):
    for j in range(0,len(lista)-2):
        for i in range(0,len(lista)-2):
            if lista[i]>lista[i+1]:
                (lista[i], lista[i+1]) = (lista[i+1], lista[i])
    return(lista)
    print(orden(list))


while True:
    m= int(input("MAX SLICES"))
    n= int(input("MAX DIFFERENT PIZZAS"))
    s=[]
    if m<1e9 or n<1e6 or m>=0 or n>=0:
        break
    else:
        print(" DEBEN CUMPLRISE: M<10^9, N<10^6")
        print(" VUELVA A INTENTARLO")
        continue

for i in range(n):
    a=int(input(f"SLICES OF PIZZA {i}:"))
    if a<=m:
       s.append(a)
    else:
        i-=1
        print(" HAS INTRODUCIDO UN NUMERO MAYOR QUE M")
        
s.sort()
print("s=",s)

u=''
ref=2**n-1
pos=ref
print(ref)
for i in range(n):
    u+='1'

print(u)
    
total=0

for i in range(ref):
    suma=0
    Lprima=[]
    for j in range(n):
        if u[j]=='1':
            suma+=s[j]
            Lprima.append(s[j])
    if suma>total and suma<=m:
        total=suma
        L=Lprima
        
    pos-=1      
    u=decimalToBinary(pos,ref)

L.sort()
print("L=",L)
print("K=",len(L))
print("Total slices:",total)    
#

    
    
    
    
    
    
    
    