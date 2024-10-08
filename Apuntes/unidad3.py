import functools
#FUNCIONES
def mi_primera_funcion():
    print("Soy la primera funcion")

def cuadrado(x):
    return x ** 2

def llama_a_la_puerta(persona, n_veces = 3):
    return ["Toc, toc " + persona + "!" for i in range(n_veces)]

#recursiva
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

#Funcion anonima o lambda
triple1 = lambda x: 3 * x

#Lambda mas complicado
def genera_multiplicador(n):
    return lambda x : x * n
doble = genera_multiplicador(2)
triple = genera_multiplicador(3)

mi_primera_funcion()
print("El cuadrado de 7 es {}".format(cuadrado(7)))
print(llama_a_la_puerta("Cinthya", 1))
print(llama_a_la_puerta("Claudia"))
fibonacci(3)
fibonacci(6)
print(doble(4))
print(triple(4))

#FUNCIONES DE ORDEN SUPERIOR
#MAP (mapear los elementos)
cuadrados = map(lambda x: x ** 2, [1,2,3,4,5])
print(list(cuadrados))
#FILTER (seleccionar elemento que cumplen una condicion)
pares = filter(lambda x: x % 2 == 0, [1,2,3,4,5])
print(list(pares))
#REDUCE un resultado reducido de los elementos
suma = functools.reduce(lambda x,y: x + y, [1,2,3,4,5])
print(suma)

#LOS EJEMPLOS DE LAS FUNCIONES DE ORDEN SUPERIOR HECHO DE OTRA FORMA
#map --- un generador
cuadrado = (x**2 for x in [1,2,3,4,5]) #lista_cuadrado [x**2 for x in [1,2,3,4,5]]
print(list(cuadrado))
#filter --- generador
pares = (x for x in [1,2,3,4,5] if x % 2 == 0) #lista_pares [x for x in [1,2,3,4,5] if x % 2 == 0]
print(list(pares))
#reduce -- bucle
otra_suma = 0
for x in [1,2,3,4,5]:
    otra_suma = otra_suma + x
print(otra_suma)
print(sum([1,2,3,4,5]))
#otras funciones
#minimo
print(min([1,2,3,4,5]))
#maximo
print(max([1,2,3,4,5]))

#MODULOS Y PAQUETES (pueden haber nombres repetidos al importar ya que cada uno tiene su namespace)
#import (nombre el modulo) as alias
#from mimodulo import funcion
#from mimodulo import *
#mimodulo.funcion(parametro)

#MODULOS DEL SISTEMA
#Interactuar con el sistema operativo
import os
#Consultas sobre nombres de ficherosy directorios
import os.path
#Acceso a variables y funciones del interprete
import sys

#MODULOS DE DATOS
#clases y funciones para fechas y horas
import datetime as dt
#formatear y hacer operaciones con fechas
import calendar

#MODULOS ADICIONALES PARA CADENAS DE TEXTO
#constantes y funciones para formatear cadenas de texto
import string
#para trabajar con expresiones regulares, busquedas...
import re

#MODULOS MATEMATICOS
#funciones matematicas
import math
#generar numeros pseudoaleatorios
import random

#MODULOS PARA PROGRAMACION FUNCIONAL
#funciones de orden superior
import functools
#iteradores para bucles
import itertools
#da operadores para funciones de orden superior en lugar de expresiones lambda
import operator as op

#MODULOS PARA FICHEROS
#iterar leyendo lineas
import fileinput as fin
#leer y escribir en ficheros CSV
import csv