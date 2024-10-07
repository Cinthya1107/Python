#CONTROL DE FLUJO
precio_chaqueta = 59.95
precio_abrigo = 140
dinero_disponible = 280
print("Tengo {} euros".format(dinero_disponible))

#IF
if((precio_chaqueta > dinero_disponible) & (precio_abrigo > dinero_disponible)):
    print("No me puedo permitir nada, ando pobre, tengo {}".format(dinero_disponible))
elif((precio_abrigo + precio_chaqueta) <= dinero_disponible):
    print("Me puedo comprar ambos, ya que tengo {}".format(dinero_disponible))
elif(precio_abrigo <= dinero_disponible):
    print("Me puedo comprar un abrigo, ya que tengo {}".format(dinero_disponible))
else:
    print("Solo me puedo comoprar la chaqueta, porque tengo {}".format(dinero_disponible))

#WHILE
i = 1
suma = 0
while i <= 10:
    suma = suma + i 
    i = i + 1
print("La suma de los primeros 10 numeros naturales vale", suma)

#FOR
lista_frutas = ["pera", "manzana", "ciruela", "cereza"]
for fruta in lista_frutas:
    print(fruta)
#secuencia de numeros con range
#incluye el primer valor y el ultimo lo excluye
suma = 0
for i in range(1, 10):
    print(i)
    suma = suma + i
print(suma)
#si solo pones un valor lo toma como el de parada
for i in range(5):
    print(str(i) * i) #str crea una cadena a partir de i
#de dos en dos
for j in range(0, 5, 2):
    print(j)

#ANIDAR BUCLES
for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end = "")
    print()

#BREAK
#calcular qué numeros son primos entre 10 y 19
for n in range(10, 20):
    print("n =", n)
    tiene_divisor = False
    for d in range(2, n):
        print("* d =", d)
        if n % d == 0:
            tiene_divisor = True
            break
    if not tiene_divisor:
        print("\t>", n, 'es primo')
#otra forma
for n in range(10, 20):
    print("n =", n)
    tiene_divisor = False
    for d in range(2, n):
        print("* d =", d)
        if n % d == 0:
            break
        else:
           print("\t>", n, 'es primo') 

#CONTINUE
#nota media de un alumno
calificaciones = ["10", "notable", None, "8", "6"]
suma = n = 0
for nota in calificaciones:
    if nota is None:
        continue
    elif not nota.isnumeric():
        continue
    else:
        suma = suma + float(nota)
        n = n + 1
print("la nota media es {}".format(suma/n))

#ESTRUCTURA DE DATOS
#LISTAS (son mutables)
#vacia
lista_vacia = []
#de numeros
lista_numeros = [1, 2, 3, 4]
#de texto 
lista_frutas
#mezcla de tipos de valores
lista_mezcla = [10, "veinte", 30.0, "cuarenta"]
#anidadas
listas_anidadas = ["Aqui hay", ["listas", "anidadas"], [1, 2]]
for elemento in listas_anidadas:
    print(elemento)
#longitud
len(lista_numeros)
len(listas_anidadas) #cuenta los elementos y sublistas
#seleccionar un elemento
lista_numeros[0]
lista_numeros[len(lista_numeros) - 1]
listas_anidadas[-1]
lista_numeros[-len(lista_numeros)]
#rebanadas
letras = ["A", "B", "C", "D", "E", "F"]
letras[0:2]
letras[2:5]
letras[2:]
letras[:4]
letras[-2:]
letras[:-2]
letras[:2] + letras[2:]
#modificar listas
print(lista_frutas)

lista_frutas[1] = "uvas"
print(lista_frutas)
#remplazar valores de una rebanada
lista_frutas[2:] = ["naranja", "aguacate"]
print(lista_frutas)
#eliminar algunos valores con una lista vacia
lista_frutas[1:3] = []
print(lista_frutas)
#vaciar la lista
lista_frutas[:] = []
print(lista_frutas)
#concatenar listas
lista_1 = ['a', 'b', 'c']
lista_2 = [100, 200, 300]
lista_1 + lista_2
#replicar listas 
3 * lista_1
#extraer elementos e introducirlos en variables
x, y, z = lista_2
print("x = ", x, "y = ", y, "z = ", z)
#añadir un elemento al final de la lista
lista_1.append('d')
print(lista_1)
#quitar el ultimo valor de la lista
ultimo_valor = lista_1.pop()
print(ultimo_valor)
print(lista_1)
#insertar un elemento en una posicion concreta
lista_1.insert(0, 'e')
lista_1.insert(2, 'c')
print(lista_1)
#buscar en que posicion esta un elemento
lista_1.index('b')
#contar el numero de veces que aparece un elemento
lista_1.count('c')
#borrar el primer elemento que coincida con el valor
lista_1.remove('c')
print(lista_1)
#ordenar la lista
lista_1.sort()
print(lista_1)
#invertir el orden de la lista
lista_1.reverse()
print(lista_1)
#borrar un elemento de una posicion concreta
del lista_1[2]
print(lista_1)
#borrar todos los elementos de la lista
lista_1.clear()
print(lista_1)
#Dos variables que apunten al mismo contenido
lista1 = [1, 2, 3]
lista2 = lista1
print(lista2)
lista1 == lista2
lista1 is lista2
#si modificamos lista2, se modifica lista1. Mismos datos, dos nombres distintos
lista2[1] = 99
print(lista1)
#pero si le asignamos una nueva lista al nombre de la variable, la otra no cambia
lista2 = [7, 8, 9]
lista2 is lista1
#aunque volvamos a referenciar a la primera lista
lista2 = 2 * lista1
lista2 is lista1
#copia identica pero independiente
lista1 = [1, 2, 3]
lista2 = lista1.copy()
lista2 == lista1
lista1 is lista2 #no es el mismo objeto

#TUPLAS (inmutables)
palos_baraja = ("corazones", "diamantes", "treboles", "picas")
valores_baraja = ('A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K')
as_de_picas = (valores_baraja[0], palos_baraja[3])
reina_de_corazones = (valores_baraja[11], palos_baraja[0])
mano =(as_de_picas, reina_de_corazones)

print(mano)
print(mano[0])
#se pueden utilizar listas como elementos
jugador = ("jugador_1", [as_de_picas, reina_de_corazones])
#se puede definir una tupla sin parentesis (no recomendable)
otra_tupla = 'uno', 'dos', 3
print(otra_tupla)
#tupla vacia
tupla_vacia = ()
#tupla con un elemento
tupla_un_elemento = (1, )

#CONJUNTOS (mutables, no ordenados, y no puede haber elementos repetidos)
#conjunto vacio
en_mochila = set()
#inicializamos
en_mochila = {"bocadillo", "agua", "linterna", "agua", "cuerda"}
print(en_mochila)
#añadimos un elemento
en_mochila.add("cuchillo")
#comprobar si un elemento esta incluido
"bocadillo" in en_mochila
#comprobar que un elemento no esta incluido
"cerillas" not in en_mochila
#quitar un elemento del conjunto
en_mochila.discard("cuerda")
print(en_mochila)
#OPERACIONES DE CONJUNTOS
a = {1, 2, 3, 5, 8}
b = {1, 2, 4, 8, 16}
#union
a.union(b)
#a (palo) b !!!!!!!!!!!!
#interseccion
a.intersection(b)
a & b
#diferencia 
a.difference(b)
a - b
#diferencia simetrica o excluyente
a.symmetric_difference(b)
#a (pico hacia arriba) b
#subconjunto
s = {1, 2}
s.issubset(a)
#s (menor o igual) a
#superconjunto
a.issuperset(s)
#a (mayor o igual) s

#DICCIONARIO (clave: valor, inmutable)
#diccionario vacio
libreta_telefonos = {}
#inicializamos
libreta_telefonos = {"Carlos" : 5556045, "Luis" : 5556048, "Javier" : 5556051}
libreta_telefonos["Luis"]
#añadir un elemento
libreta_telefonos["Daniel"] = 5556056
#cambiar un valor
libreta_telefonos["Carlos"] = 5556033
#comprobar si una clave esta en el diccionario
"Luis" in libreta_telefonos
#eliminar un elemento
del libreta_telefonos["Luis"]
print(libreta_telefonos)
#ITERAR
#Claves
for nombre in libreta_telefonos:
    print(nombre, "=", libreta_telefonos[nombre])
#por parejas
for nombre, telefono in libreta_telefonos.items():
    print(nombre, "=", telefono)
#Valores
for telefono in libreta_telefonos.values():
    print(telefono)

#DEFINICIONES POR COMPRENSION (construir una coleccion a partir de otra)
tabla_7 = []
#iteramos
for i in range(0,11):
    tabla_7.append(7 * i)
print(tabla_7)
#lo anterior de una forma resumida
tabla_7 = [7 * x for x in range(0, 11)]
print(tabla_7)
#solo cuando el multiplicador sea par
tabla_7 = [7 * x for x in range(0, 11) if x % 2 == 0]
print(tabla_7)
#otro ejemplo
lista_frutas = ["pera", "manzana", "cereza", "ciruela"]
lista_frutas = [fruta.upper() for fruta in lista_frutas if fruta.startswith('c')]
print(lista_frutas)
#otro ejemplo
[x * y for x in (1, 2, 3) for y in (4, 5, 6)]
#ejemplo de for anidados
[ (x, y, x * y) for x in (1, 2, 3) for y in (4, 5, 6)]
#en vez de lista, construir un conjunto
{ x for x in range(10) if x % 2 != 0}
#si queremos una tupla
tuple( x for x in range(5))
#un diccionario
diccionario_tabla_7 = { num : 7 * num for num in range(0, 11)}

#GENERADOR (hace calculos, iterando sobre la coleccion de entrada)
generador_tabla_7 = (7 * x for x in range(0, 11))
print(generador_tabla_7)
#sacar los valores en un bucle
for v in generador_tabla_7:
    print(v)
#extraer los valores a una lista
generador_tabla_3 = (3 * x for x in range(0, 10))
lista_tabla_3 = list(generador_tabla_3)
print(lista_tabla_3) #si lo intentas meter en otra lista, se genera una vacia