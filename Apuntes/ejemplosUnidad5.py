#ARRAYS
#Ejemplo

#Calcular indice de grasa
altura = [1.67, 1.73, 1.76, 1.85, 1.77, 1.73]
masa = [65.0, 79.2, 76.7, 82.0, 72.5, 66.1]
#Si intentamos operar con las listas directamente, no funcionará
#masa / (altura**2)

#Maneras de hacerlo
#Iterar los valores en un bucle
imc = []
for i in range(len(altura)): 
    a = altura[i] 
    m = masa[i] 
    imc.append(m/(a**2)) 
print(imc)

#Usar map()
imc = list(map(lambda m, a : m/(a**2), masa, altura))
print(imc)

#Cuando hay que emparejar valores de listas distintas para formar tuplas, tambien podemos usar la función zip()
imc = [m/(a**2) for m, a in zip(masa, altura)]
print(imc)

#Con Numpy
import numpy as np
#Definimos los arrays
vAltura = np.array([1.67, 1.73, 1.76, 1.85, 1.77, 1.73])
vMasa = np.array([65.0, 79.2, 76.7, 82.0, 72.5, 66.1])
#Calculamos
imc = vMasa/(vAltura ** 2)
print("Numpy", imc)

#ARRAYS
#Vector (una dimensión)
v_1d = np.array([1,2,3])
#Mostrar número de dimensiones
print(v_1d.ndim)
#Número de elementos en cada dimensión del array
print(v_1d.shape)
#Número total de elementos del array
print(v_1d.size)
#Tipo de los elementos
print(v_1d.dtype)

#Crear una matríz utilizando listas anidadas
m_2d = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
print(m_2d)
print(m_2d.ndim)
print(m_2d.shape)
print(m_2d.size)
print(m_2d.dtype)

#Indicar el tipo de dato de los elementos al crear el array
dtype = np.array([[1,2,3],[4,5,6]])
dtype = 'float64'
print(dtype)

#Función crear arrays en vez ded listas, (no incluye el último número)
m1 = np.arange(15)
print(m1)
#Indicar el limite inicial, final y el tamaño del paso
m2 = np.arange(1, 10, 2)
print(m2)

#Crear un array dividiendo un intervalo
m3 = np.linspace(0, 10, 5)
print(m3)

#Crear un vestor con 5 ceros
zero = np.zeros(5)
print(zero)
#Crear una matríz de 2x3 de ceros
zeros =np.zeros((2,3))
print(zeros)
#Crear una matríz 2x3 de unos
ones = np.ones((2,3))
print(ones)
#Crear una matríz rellenada con el mismo valor para todos elementos
eleven_full = np.full((2,3), 11)
print(eleven_full)
#Crear una matríz identidad 3x3 (1 en la diagonal, 0 en el resto)
identidad = np.eye(3)
print(identidad)
#Crear una semilla de números aleatorios reproducibles (siempre los mismos)
seed = np.random.seed(42)
#Distribución uniforme [a, b)
distribucion_uniforme = np.random.uniform(0, 10, size=(2,3))
print(distribucion_uniforme)
#Distribución normal (media = 0, desviación típica = 1)
distribucion_normal = np.random.normal(0,1, size=(2,3))
print(distribucion_normal)
#Crear un array con remplazo (permitiendo valores replicados)
vbase = np.arange(10)
remplazo = np.random.choice(vbase, size=8, replace=True)
print(vbase)
print(remplazo)
#Sin remplazo
no_remplazo = np.random.choice(vbase, size=8, replace=False)
print(no_remplazo)

#INDEXADO E ITERACIÓN
#Vector
v1 = np.arange(0,50,5)
print(v1)

#Seleccionar un elemento individual
print(v1[2])
#Varios
print(v1[[1,4,8]])
#Con una matriz 3x4
m2 = np.array([range (0,4), range(4,8), range(8,12)])
print(m2)

#Seleccionamos un elemento indicando la fila(2) y columna(3)
print(m2[2,3])
#Seleccionamos todos los elementos de la fila 1 y 2 (:)
print(m2[[1,2], :])
#Seleccionamos los elementos de la fila 1 en las columnas 2 y 3
print(m2[1, [2,3]])
#Seleccionamos la fila 0
print(m2[0, :])
#Seleccionamos la columna 1
print(m2[:, 1])
#Seleccionamos los elemntos que estáne entre la fila 1 y 3 (no incluida), y las columnas 1 y 3
print(m2[1:3, 1:3])

#MASCARAS
#Comprobamos que elemento del array es par
mascara_pares = (m2 % 2 == 0)
print(mascara_pares)
print(m2[mascara_pares])
#Resumido en una expresión
print(m2[m2 % 2 == 0])

#MANIPULANDO ARRAYS
#Creamos un vector y una matriz
v = np.arange(15)
m = v.reshape(3,5)
print(v)
print(m)
#Obtener otro vector "aplanando la matriz"
v2 = m.flatten()
print(v2)
#Transponer la matriz
print(m.T)

#Apilar matrices
m1 = np.arange(0,6).reshape(2,3)
m2 = np.arange(10,16).reshape(2,3)
print(m1)
print(m2)
#Verticalmente
vertical = np.vstack((m1, m2))
print(vertical)
#Horizontalmente
horizontal = np.hstack((m1, m2))
print(horizontal)

#Añadir al final una fila
fila = np.array([30, 40, 60])
new_fila = np.vstack((m1, fila))
print(new_fila)
#Añadir una columna
columna = np.array([100, 200])
new_column = np.column_stack((m1, columna))
print(new_column)

#Dividir el array
m_grande = np.arange(12).reshape(3, 4)
print(m_grande)
#Horizontalmente en dos trozos
divh = np.hsplit(m_grande, 2)
print(divh[0])
print(divh[1])
#Verticales, podemos indicar puntos de división con una tupla
divv = np.vsplit(m_grande, (1,))
print(divv[0])
print(divv[1])

#OPERANDO CON ARRAYS
#ASIGNACIONES
m = np.arange(12).reshape(3, 4)
print(m)
#Cambiar un elemento en particular
m[0,0] = 100
print(m)
#Cambiar una "rebanada" por una lista de valores
m[1, 1:] = [50, 60, 70]
print(m)
#Cambiar todos los elementos seleccionados por un único valor
m[1:, 2:] = 0
print(m)

#OPERACIONES MÁTEMATICAS
v1 = np.array([2,5])
v2 = np.array([3,3])
m1 = np.array([1,2,3,4]).reshape(2,2)
m2 = np.array([3,5,7,11]).reshape(2,2)
#Escalar todos los elementos
print(v1 + 3)
print(m1 + 5)
#Sumar dos arrays, elemento a elemento
print(m1 + m2)
#Resta
print(m2 - m1)
#Multiplicación con escalar
m10 = 10 * m1
print(m10)
#Multiplicación de arrays
print(v1 * v2)
print(m1 * m2)
#División 
print(m10 / m1)
#Arrays
v1 = np.array([2,5])
v3 = np.array([3,3,3])
m1 = np.array([1,2,3,4]).reshape(2,2)

#Multiplicar matriz 2x2 por vector
print(m1 * v1)
#Es como tener el vector 2 apilado dos veces
mv1 = np.vstack((v1, v1))
print(mv1)
print(m1 * mv1)
#No se pueden con distintas dimensiones, y con tamaños no compatibles
#print(m1 * v3)

#Raíz cuadrada
print(np.sqrt(m1))
#Funciones trigonométricas
print(np.sin(m1))
print(np.cos(m1))
print(np.tan(m1))
#Logaritmos
print(np.log(m1))
#Exponencial
print(np.exp(m1))

#OPERACIONES DE AGREGACIÓN Y ESTADÍSTICA
m3 = np.arange(1,10).reshape(3,3)
print(m3)
#Suma de todos los elementos de un array
suma = np.sum(m3)
print(suma)
#Suma de loss elementos de cada columna
sum_column = np.sum(m3, axis = 0)
print(sum_column)
#Suma de los elemntos de cada fila 
sum_fila = np.sum(m3, axis = 1)
print(sum_fila)
#Media
media = np.mean(m3, axis=0)
print(media)
#Desviación estandar
desv_est = np.std(m3)
print(desv_est)
#Máximos y mínimos
min = np.min(m3, axis=0)
max = np.max(m3, axis=1)
median = np.median(m3)
print(min)
print(max)
print(median)
#Suma acumulada de elementos
suma_acumulada = np.cumsum(m3)
suma_acumulada1 = np.cumsum(m3, axis=0)
print(suma_acumulada)
print(suma_acumulada1)

#ÁLGEBRA Y VESCTORES Y MATRICES
m1 = np.array([1,3,4,7,5,8,2,9,6]).reshape(3,3)
print(m1)
#Transponer la matriz 
transp = m1.transpose()
m1.T
print(transp)
#Matriz onversa
m1_inv = np.linalg.inv(m1)
print(m1_inv)
#Traza de la matriz (suma de elementos de la diagonal principal)
traza = m1.trace()
print(traza)
#Producto interior de dos vectores
v1 = np.array([1,4,6])
v2 = np.array([3,5,2])
vp1 = v1.dot(v2)
print(vp1)
#Con matrices
m1 = np.array([4,1,1,2]).reshape(2,2)
m2 = np.array([1,3,5,1]).reshape(2,2)
mp1 = m1.dot(m2)
print(mp1)
#Vector y Matriz
v3 = np.array([3,5])
mv = m1.dot(v3)
print(mv)

#COPIAS Y VISTAS Y ARRAYS
#Referencias
v1 = np.arange(10)
print(v1)
#v1 y v2 son referencias que apuntan al mismo contenido
v2 = v1
v2[3] = 999
print(v2 is v1)

#Vista
v1 = np.arange(12)
print(v1)
m1 = v1.reshape(3,4)
print(m1)
#Ver el array de partida
print(m1.base is v1)
#Modificamos el primer array
m1.shape = (4,3)
print(m1)
#No cambiamos la forma del original
v1.shape
print(v1)
#Si modificamos el valor de un elemento
m1[0, 2] = 999
print(m1)
#modificamos los datos del original
print(v1)

#COPIA PROFUNDA
v1 = np.arange(10)
print(v1)
#Creamos una copia nueva
v2 = v1.copy()
print(v2)
#Son estructuras distintas e independientes
print(v2.base is v1)
#Modificamos uno 
v2[0] = 9999
print(v2)
print(v1)

#LEYENDO FICHEROS
#matriz = np.genfromtxt(fname = "ruta", delimiter=";", skip_header= 0)
#print(matriz)

