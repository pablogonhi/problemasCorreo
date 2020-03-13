# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 13:40:00 2020

@author: pablo
"""

import numpy as np
from collections import defaultdict

def buscador(x,y,R,C, ma3pa):
        candidatos=[]
        for j in range(0,R):          ##J ES LA FILA R PRIMA
            for k in range(0,C):     ##K ES LA COLUMNA C PRIMA    
                if x==j or y==k or x-y==j-k or x+y==j+k:
                    pass
                else:
                    if mapa[j][k]==0:   
                        candidatos.append([j,k])
                        break
                    else:
                        pass

        return candidatos


                    
historial = defaultdict(list)

R=int(input("NUMERO DE FILAS:"))
C=int(input("NUMERO DE COLUMNAS:"))
n=R*C

#
#A = np.array([[1, 2, 3], [3, 4, 5]])
#print(A)
#
#A = np.array([[1.1, 2, 3], [3, 4, 5]]) # Array of floats
#print(A)
#
#A = np.array([[1, 2, 3], [3, 4, 5]], dtype = complex) # Array of complex numbers
#print(A)
mapa=np.zeros((R,C))
intento=np.zeros((n))
posibilidades=np.zeros((n))
x=int(input("Fila de inicio (del 1 al NºFILAS):"))-1
y=int(input("Columna de inicio (del 1 al Nº COLUMNAS):"))-1

status=0
cuenta=0
iteracion=0
candidatos=[]
camino=[[]]*n

numcan=[0]*n
mapa[x][y]=1
print(mapa)
camino[0]=[x,y]


while True:
    iteracion+=1
    print(camino)
    i=cuenta
    print("PASO",i," - ITERACION:", iteracion)
    candidatos=buscador(x,y,R,C, mapa)
    historial[i]=candidatos
    posibilidades[i]=len(candidatos)
    print("CANDIDATOS EN EL PASO",i,": ",candidatos)
    if candidatos==[]:
        cuenta-=1
        intento[i-1]+=1
        intento[i]=0
        x,y=camino[i]
        mapa[x][y]=0
        posibilidades[i]=0
        camino[i]=[]
        try:
            x,y=camino[i-1]
        except ValueError:
            print("-------------------------------------")
            print("RESULTADO FINAL")
            print("ES IMPOSIBLE")
            break
        print(mapa)
        for m in range(i,n):
            historial[i].clear()
        print(historial)
        print("BUSCA")
        
        continue
    
    
    i=cuenta
    
    if 0 in mapa and intento[i]>(posibilidades[i]-1):
       print("NO QUEDAN POSIBILIDADES, RETROCEDEMOS")
       mapa[x][y]=2    
       cuenta-=1
       intento[i-1]+=1
       intento[i]=0
       posibilidades[i]=0
       x,y=camino[i]
       mapa[x][y]=0
       camino[i]=[]
       try:
           x,y=camino[i-1]
       except ValueError:
          print("-------------------------------------")
          print("RESULTADO FINAL")
          print("ES IMPOSIBLE")
          break
           
       for m in range(i,n):
           historial[i].clear()
       print(mapa)
    else:
        try:
    #    if historial[i][int(intento[i])]!=[]:
            x,y=historial[i][int(intento[i])]
            if int(mapa[x][y])==0:
                print("AVANZAMOS EN EL CAMINO", [x,y])
                mapa[x][y]=1
                camino[i+1]=[x,y]
                cuenta+=1
                print(mapa)
        except IndexError:
          print(intento[i])
          intento[i]+=1
          print("INCREMENTO DE INTENTO",(intento[i]-1), " A", intento[i],"EN EL PASO:",i)
          
          
    if not 0 in mapa:
          print("-------------------------------------")
          print("RESULTADO FINAL")
          print("ES POSIBLE")
          print("HISTORIAL DE POSIBILIDADES:",historial)
          print("------------------------------")
          print("EL CAMINO A SEGUIR POR LA NAVE ES: ",camino)
          break        