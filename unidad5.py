#CALCULO CIENTIFICO: NUMPY
#Cal cular el IMC
altura = [1.67, 1.73, 1.76, 1.85, 1.77, 1.73]
masa = [65.0, 79.2, 76.7, 82.0, 72.5, 66.1]

imc = []
for i in range(len(altura)):
    a = altura[i]
    m = masa[i]
    imc.append(m/(a**2))
print(imc)
#tambien se puede usar Map
list( map(lambda m,a : m/(a**2), masa, altura))
#podemos usar zip para emparrejar valores de listas distintas para formar una tupla
[m/(a**2) for m,a in zip(masa, altura)]

#Con NUMPY
import numpy as np
valtura = np.array([1.67, 1.73, 1.76, 1.85, 1.77, 1.73])
vmasa = np.array([65.0, 79.2, 76.7, 82.0, 72.5, 66.1])
vmasa / (valtura ** 2)
#Arrays
v_1d = np.array([1,2,3])
#numero de dimensiones
print(v_1d.ndim)
#numero de elementos por dimension
print(v_1d.shape) #si son mas dimensiones (filas, columnas)
#numero total de elementos en un array
print(v_1d.size)
#tipo de elementos
print(v_1d.dtype)
#indicar el tipo de elementos
print(np.array([[1,2,3],[4,5,6]], dtype='float'))
#funcion que crea arrays
m1 = np.arange(15)
print(m1)
m2 = np.arange(1, 10, 2)
print(m2)
#cree un numero de elementos en el array de un rango
m3 = np.linspace(0, 10, 5)
print(m3)
#crear un vector de 0
print(np.zeros(5))
print(np.zeros((2,3)))
#crear un vector de unos
print(np.ones((2,3)))
#crear un vestor relleno de un valor especifico
print(np.full((2,3), 99))
#creacr una matriz identidad
print(np.eye(3))
# ?????
print(np.random.seed(42))
#crear una matriz con numeros aleatorios de [0,1)
print(np.random.random((2,3)))
#distribucion uniforma
print(np.random.uniform(0, 10, size=(2,3)))
#distribucion normal (media = 0, desviacion tipica= 1)
print(np.random.normal(0,1, size=(2,3)))
#cambiar valores de un array
vbase = np.arange(10)
print(vbase)
print(np.random.choice(vbase, size=8, replace=True)) #permite valores replicados
print(np.random.choice(vbase, size=8, replace=False)) #no permite valores replicados
#seleccionr un elemento individual
v1 = np.arange(0, 50, 5)
print(v1)
print(v1[2])
#seleccionar varios a la vez
print(v1[[1, 4, 8]])
#lo mismo con varias dimensiones
m2 = np.array([range(0,4), range(4,8), range(8, 12)])
print(m2)
print(m2[2,3])#Fila y columna
#seleccionar todos los elementos de las filas 1 y 2
print(m2[[1,2], :])
#seleccionar los elementos de la fila 1 y columnas 2 y 3
print(m2[1, [2,3]])
#otras opciones de seleccion
print(m2[0, :])
print(m2[:, 1])
print(m2[1:3, 1:3])#elementos entre la fila y columna 1 y 3 in incluir
#mascara booleana
mascara_pares = (m2 % 2 == 0)
print(mascara_pares)
print(m2[mascara_pares]) #m2[m2 % 2 == 0] 
#crear un array multidimensional a partir de un vector
v = np.arange(15)
print(v)
m = v.reshape(3, 5)
print(m)
#apalanar una matriz
v = m.flatten() #v = m.flatten('F')
print(v)
#transponer una matriz
print(m.T)
#concatenar/apilar arrays
m4 = np.arange(0,6).reshape(2,3)
m5 = np.arange(10, 16).reshape(2,3)
stacked_vertical = np.vstack((m4,m5))
print(stacked_vertical)
#apilar horizontalmente
print(np.hstack(m5))#?????' deberian ser 2
#añadir una fila al final del array ????
fila = np.array([30, 40, 60])
array_fila_mas =np.vstack((m4, fila))
print(array_fila_mas)
#añadir una columna
columna = np.array([100, 200, 300, 400, 500])
columna_mas =np.column_stack((m3, columna))
print(columna_mas)
#dividir un array
m_grande = np.arange(12).reshape(3, 4)
print(m_grande)
divh = np.hsplit(m_grande, 2) #horizontalmente en dos
print(divh[0])#primer trozo
print(divh[1])#segundo trozo
#dividir verticalmente
divv = np.vsplit(m_grande, (1,))#podemos indicar los puntos de division
print(divv[0])
print(divv[1])
#modificar arrays
m = np.arange(12).reshape(3,4)
print(m)
#cambiar un elemento en particular
m[0, 0] = 100
print(m)
#cambiar una rebanada
m[1, 1: ] = [50, 60, 70]
print(m)
#cambiar todos los elementos seleccionados
m[1: ,2: ] = 0
print(m)
#operaciones matematicas (elemento a elemento)(siempre el mismo numero de dimensiones)
v1 = np.array([2,5])
v2 = np.array([3,3])

m1 = np.array([1,2,3,4]).reshape(2,2)
m2 = np.array([3,5,7,11]).reshape(2,2)
#sumar un escalar
print(v1 + 3)
print(m1 + 5)
#sumar dos arrays elemento a elemento 
print(m1 + m2)
#resta de arrays
print(m2 - m1)
#multiplicación con escalar
m10 = 10 * m1
print(m10)
#multiplicacion con arrays
print(v1 * v2)
print(m1 * m2)
#división
print(m10 / m1)
#raíz cuadrada
print(np.sqrt(m1))
#funciones trigonométricas
print(np.sin(m1))
print(np.cos(m1))
print(np.tan(m1))
#logaritmo
print(np.log(m1))
#exponencial
print(np.exp(m1))
#Operaciones de agrgación y estadisticas
#sumar todos los elementos de  un array
m3 = np.arange(1,10).reshape(3,3)
print(m3)
np.sum(m3)
#sumar los elementos de cada columna 
np.sum(m3, axis = 0)
#sumar los elementos de cada fila
np.sum(m3, axis = 1)
#media
np.mean(m3)
np.mean(m3, axis = 0)
#desviacion estándar
np.std(m3)
#máximos y mínimos
np.max(m3, axis = 1)
np.min(m3, axis = 0)
np.median(m3) #??????
#suma acumulada de elementos
np.cumsum(m3)
np.cumsum(m3, axis = 0)
#Algebra de vestores y matrices
m1 = np.array([1, 3, 4, 7, 5, 8, 2, 9, 6]).reshape(3,3)
print(m1)
#transponer una matriz
m1.transpose()
m1.T #Igual, mas breve
#calcular la inversa
m1_inv = np.linalg.inv(m1)
print(m1_inv)
#traza de la matriz
m1.trace()
#el producto interior de una matriz y un vector es un vector
"""v3 = np.array([3, 5])
mv = m1.dot(v3)
print(mv)"""
#Crear una nueva referencia a un array
v1 = np.arange(10)
print(v1)
v2 = v1
v2[3] = 999
print(v1)
v2 is v1
#Vista (copia superficial)
v1 = np.arange(12)
print(v1)
#version manipulada de array
m1 = v1.reshape(3, 4)
print(m1)
#comprobamos que ambos arrays apuntan al mismo contenido
m1.base is v1
#si modificamos el segundo array
m1.shape = (4,3)
print(m1)
#no se modifica el otro
v1.shape
print(m1)
#pero si modificamos el dato de un elemento
m1[0, 2] = 999
print(m1)
#modificamos tambien el original
print(v1)
#Copia profunda (no comparte memoria con el array original)
v1 = np.arange(10)
print(v1)
v2 = v1.copy()
print(v2)
#como son estructuras diferentes
v2.base is v1
#si se cambia el valor de un elemento
v2[0] = 999
print(v2)
print(v1)
#Leer ficheros
matriz = np.genfromtxt(fname = "./U09_datasets/ejemplo_numpy_datos.csv", delimiter = ";", skip_header = 0)
print(matriz) 