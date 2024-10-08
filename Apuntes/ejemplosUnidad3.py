#FUNCIONES
# Definimos una funcion
def mi_primera_funcion():
    print("Soy la primera funcion")
#Funcion que devuelve el cuadrado del numero x que pasamos como argumento
def cuadrado(x):
    """Devuelve el cuadrado de x"""
    return x**2
# Funcion con dos parametros
def llama_a_la_puerta_de(persona, n_veces):
    """Llama a la puerta de la persona las veces que haga falta"""
    return [ "Abreeeeeeeee " + persona + "!" for i in range(n_veces)]
# Se puede definir un parametro por defecto por si no se introduce un valor
def llama_a_la_puerta_de(persona, n_veces = 2):
    """Llama a la puerta de la persona las veces que haga falta"""
    return [ "Abreeeeeeeee " + persona + "!" for i in range(n_veces)]

# Invocar la funcion
mi_primera_funcion()
# Prueba de la funcion cuadrado(x)
print("El cuadrado de 10 es: ", cuadrado(10))
print("El cuadrado de 7 es: ", cuadrado(7))
# Prueba de la funcion llama_a_la_puerta_de
print(llama_a_la_puerta_de("Cinthya", 7))
print(llama_a_la_puerta_de("Pepe"))
print(llama_a_la_puerta_de(n_veces=3, persona="Howard")) #Si indicamos el parametro da igual el orden

#RECURSION (una funcion se llame a si misma)
def fibonacci(n):
    """Calcula el n-esimo elemento de la serie de Fibonacci"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(3))
print(fibonacci(6))

#FUNCIONES ANONIMAS (solo pueden devolver un valor)
# Creamos una funcion anonima y se lo asignamos a la variable triple
triple = lambda x: 3 * x
print(triple(5))
# Ejemplo de un codigo mas grande
# Funcion que busca un multiplicador y multiplica ese numero por el valor
def genera_multiplicador(n):
    return lambda x: x * n
# Funcion que multiplica todo por dos
doble = genera_multiplicador(2)
print(doble(3))
print(doble(5))
print(triple(7))
print(triple(9))

#FUNCIONES DE ORDEN SUPERIOR (reciben funciones o las devuelven)
# MAP
cuadrados = map(lambda x: x**2, [1,2,3,4,5]) # Combina ambos elementos
print(list(cuadrados)) # Los ordena en una lista

# calcular cuadrados usando un generador
cuadrados_2 = (x**2 for x in [1,2,3,4,5])
print(list(cuadrados_2))
# la lista directamente
lista_cuadrados = [x**2 for x in [1,2,3,4,5]]
print(lista_cuadrados)

# FILTER (siempre devuelve true o false)
pares = filter(lambda x: x % 2 == 0, [1,2,3,4,5])
print(list(pares))

# con un generador
pares_2 = (x for x in [1,2,3,4,5] if x % 2 == 0)
print(list(pares_2))
# lista directamente
lista_pares = [x for x in [1,2,3,4,5] if x % 2 == 0]
print(lista_pares)

# REDUCE (solo devuelve un unico valor)
import functools #Hay que descargar la libreria
suma = functools.reduce(lambda x,y: x + y, [1,2,3,4,5])
print(suma) #(1+2)+(3+3)+(6+4)+(10+5) hasta que se agoten los elementos

# usando un bucle
otra_suma = 0
for x in [1,2,3,4,5]:
    otra_suma = otra_suma + x
print(otra_suma)

#OTRAS FUNCIONES
print(sum([1,2,3,4,5]))
print(min([1,2,3,4,5]))
print(max([1,2,3,4,5]))

#////////////////////////////////////
#MODULOS Y PAQUETES TEMARIO EN mimodulo.py
#Importar un modulo y usar una funcion
import mimodulo as m
print(m.fibonacci(10))
#Solo coger una variable
from mimodulo import doblar
print(doblar(7))
#Si tiene el mismo nombre que una funcion local, renombramos
from mimodulo import triplicar as triple
print(triple(5))
#Podemos importar todo
from mimodulo import *

#Ejemplo de modulos ejecutables
#Cuerpo principal ejecutable, si estamos dentro del namespace __main__
if __name__ == "__main__":
    print("Ejecutamos el main")
    print(llama_a_la_puerta_de("Leyre"))

#MODULOS DEL SISTEMA
#os (funciones basicas para acceder e interactuar al sistema operativo)
import os
#os.path (realizar consultas sobre nombres de ficheros y directorios)
import os.path
#sys (acceso a variables y funciones relacionadas con el interprete y su estado)
import sys

#MODULOS DE TIPOS DE DATOS
#datetime (clases y funciones basicas para manipular fechas y horas)
import datetime as dt
#calendar (formatear y hacer operaciones con fechas de calendario)

#MODULOS ADICIONALES PARA CADENAS DE TEXTO
#string (constantes y funciones adicionales para formatear cadenas de texto)
import string
#re (trabajar con expresiones regulares. busqueda, extracciones y sustituciones de cadenas de texto)
import re

#MODULOS MATEMATICOS
#math
import math
#random (genera numeros pseudoaleatorios, distribuciones de probabilidad...)

#MODULOS PARA PROGRAMACION FUNCIONAL
#functools (utilidades para facilitar el trabajo con funciones de orden superior)
import functools as fn 
#intertools (iteradores para construir bucles)
import intertools as it 
#operator (sustituye las expresiones lambda)
import operator as op 

#MODULOS PARA FICHEROS
#fileinput (iterar leyendo lineas de uno o mas ficheros de entrada)
import fileinput as fin 
#csv (leer y escribir ficheros en formato CSV)
import csv
