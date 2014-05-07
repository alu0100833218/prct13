#!/usr/bin/python
#! encoding: UTF-8

import time
import timeit
import modulo


lista=[]

def error(intervalos,test,umbral):
  fallos=0
  for i in range (test):
    s=modulo.f(intervalos)
    error=abs(s-modulo.PI)
    if error>=umbral:
      fallos=fallos+1
  return ((fallos/test)*100)

if __name__=="__main__":
   import sys
   
   if((len(sys.argv) == 1) or (len(sys.argv) == 2) or (len(sys.argv) == 3)):
     print("No ha introducido todos los argumentos, se usarán los estándar")
     n=100
     v=10
     p=0.00001
     
   else:
     n=int(sys.argv[1])
     v=int(sys.argv[2])
     p=float(sys.argv[3])
   
   t_upla_intervalos=(10, 50, 100, 150, 500, 550, 1000)
   lista_tiempo=[]
   for i in t_upla_intervalos:
     start=time.time()
     s=error(i,v,p)
     finish=time.time()-start
     lista_tiempo=lista_tiempo+[finish]
     print "El porcentaje de error es: %5.3f" %s
     print "El tiempo que tardó el proceso es de: %14.13f" %finish
   lista=lista+[finish]
   print "Proporcione un nombre para el fichero donde se guardarán los resultados:"
   nombre_fichero= raw_input();
   f=open(nombre_fichero, 'w')
   f.write('El tiempo final es:')
   f.write(str(lista[0]) + '\n')
   f.close()
   
import matplotlib.pyplot as pl

pl.plot(t_upla_intervalos, lista_tiempo, '--d')
pl.xticks([10,50,100,150,500,550,1000])
pl.xlim(-10.0,1100.0)  
pl.ylim(-0.001,0.014)
pl.xlabel('Intervalos')
pl.ylabel('Tiempos en segundos')
pl.title('Tiempo')
pl.savefig("graficapi.eps", dpi=72)
pl.show()
