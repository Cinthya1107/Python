#CONDICIONALES
print("///////CONDICIONALES////////")
precio_chaqueta = 59.95
precio_abrigo = 140
dinero_disponible = 100
print("Tengo {} euros".format(dinero_disponible))
# Comprobamos la condición
if precio_abrigo <= dinero_disponible:
    print("El abrigo cuesta menos de {} euros".format(dinero_disponible))
elif precio_chaqueta <= dinero_disponible:
    print("La chaqueta cuesta menos de {} euros".format(dinero_disponible))
else:
    print("La chaqueta y el abrigo valen mas que {} euros".format(dinero_disponible))

#BUCLES
print("///////BUCLES////////")
i = 1
suma = 0
print("///////WHILE////////")
while i <= 10:
    suma = suma + i
    i = i + 1
print("La suma de los 10 primeros números naturales vale ", suma)

lista_frutas = ["pera", "manzana", "ciruela", "cereza"]

print("///////FOR////////")
print("Primer FOR")
for fruta in lista_frutas:
    print(fruta)

# Iterar secuencia de números
print("Segundo FOR")
suma = 0
for i in range(1, 10):
    print(i)
    suma = suma + i
print(suma)

# Generamos una secuencia indicando solo el valor de parada (para en el 4)
print("Tercero FOR")
for i in range(5):
    print(str(i) * (i)) # str(x) crea una cadena a partir de x

# Generar secuencia de dos en dos
print("Cuarto FOR")
for j in range(1, 10, 2):
    print(j)

#BREAK, CONTINUE Y BUCLES ANIDADOS
print("///////////BREAK, CONTINUE Y BUCLES ANIDADOS///////////")
for i in range(1, 5):
    for j in range(1, i+1):
        print(j, end= " ")
print()

# Calcular qué números son primos entre 10 y 19
for n in range(10, 20):
    print("n = ", n)
    tiene_divisor = False
    for d in range(2, n):
        print("* d = ", d)
        if n % d == 0:
            tiene_divisor = True
            break
    if not tiene_divisor:
        print(" --> ", n, "es primo")

#Otra manera de calcularlo
for n in range(10, 20):
    print("n = ", n)
    for d in range(2, n):
        print("* d = ", d)
        if n % d == 0:
            break
        else:
            print(" > ", n, "es primo")

# Calcular nota media un alumno
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
print("La nota media es", (suma/n))

#Listas
print("///////////LISTAS///////////")
lista_vacia = []
lista_nums = [1, 6, 2, 5, 3, 4]
lista_mezcla = [10, "veinte", 30.0, "cuarenta"]
listas_anidadas = ["Aquí hay", ["listas", "anidadas"], [1, 2]]

for elemento in listas_anidadas:
    print(elemento)

# Longitud de la lista
print(len(lista_nums))
# Longitud de la lista anidada (las sublistas las cuenta como un elemento único)
print(len(listas_anidadas))
# Seleccionar un elemento
print(lista_nums[0])
# Seleccionar el último elemento
print(lista_nums[len(lista_nums) - 1])
# Al seleccionar en una lista anidada
print(listas_anidadas[1])
# Usando números negativos empieza a contar desde atras
print(lista_nums[-1])
# Devuelbe el primer elemento de la lista
print(lista_nums[-len(lista_nums)])

print("///////////ELEMENTOS LISTAS///////////")
letras = ['A','B','C','D','E','F']
# Seleccionamos una "rebana" con los dos primeros elementos
print(letras[0:2])
# Si no especificas el final, selecciona hasta el final
print(letras[2:])
# Si no especificas el principio imprime desde la primera posición
print(letras[:4])

# Seleccionamos desde la penúltima posición hasta el final
print(letras[-2:])
# Seleccionamos hasta la penúltima posición
print(letras[:-2])

# El primer indice siempre se incluye y el último siempre se excluye
print(letras[:2] + letras[2:])

print("///////////LISTAS MUTABLES///////////")
print(lista_frutas)
# Modificar 
lista_frutas[1] = "uva"
print(lista_frutas)
# Modificar una rebanada
lista_frutas[2:] = ["naranja", "aguacate"]
print(lista_frutas)
# Borrar algunos valores
lista_frutas[1:3] = []
print(lista_frutas)
# Borrarla entera
lista_frutas[:] = []
print(lista_frutas)

# Concatenar listas
lista_1 = ["a", "b", "c"]
lista_2 = [100, 200, 300]
print(lista_1 + lista_2)
# Replicar
print(3 * lista_1)
# Extraer elementos de una lista y asignarlos a una variable
x, y, z = lista_2
print(x)
print(y)
print(z)

# Métodos para listas
# Añadir un elemento al final de la lista
lista_1.append("d")
print(lista_1)
# Extraer el último elemento
ultimo_valor = lista_1.pop()
print(ultimo_valor)
print(lista_1)
# Insertar un elemento en una posición concreta
lista_1.insert(0, "e")
lista_1.insert(2, "c")
print(lista_1)
# Buscar en que posición está un elemento
lista_1.index("b")
print(lista_1)
# Contar el número de veces que aparece un elemento
lista_1.count("c")
print(lista_1)
# Borrar el primer elemento que coincida con el valor
lista_1.remove("c")
print(lista_1)
# Ordenar
lista_1.sort()
print(lista_1)
# Invertir el orden
lista_1.reverse()
print(lista_1)
# Borrar por posición
del lista_1[2]
print(lista_1)
# Limpiar todos los elementos de la lista
lista_1.clear()
print(lista_1)

# Igualar listas
lista1 = [1, 2, 3]
lista2 = lista1
print(lista2)

lista2 is lista1

# Hacer una copia exacta
lista3 = lista1.copy()
lista3 == lista1

# TUPLAS (NO SE PUEDEN CAMBIAR SUS ELEMENTOS)
palos_baraja = ("corazones","diamantes","tréboles","picas")
valores_baraja = ('A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K')
as_de_picas = (valores_baraja[0], palos_baraja[3])
reina_de_corazones = (valores_baraja[11], palos_baraja[0])
# Anidar
mano = (as_de_picas, reina_de_corazones)
print(mano)
# Se pueden usar listas de elementos
jugador = ("jugador_1", [as_de_picas, reina_de_corazones])
print(jugador)
# Se deben usar parantesís para definir tuplas pero no son necesarios
otra_tupla = 'uno','dos',3
print(otra_tupla)
# Tupla vacia
tupla_vacia = ()
print(tupla_vacia)
# Con un elemento
tupla_un_elemento = (1,)
print(tupla_un_elemento)

# CONJUNTOS
# Conjunto vacío
en_mochila = set()
# Inicializar
en_mochila = {"bocadillo", "agua", "linterna", "agua", "cuerda"}
print(en_mochila) # el agua no se duplica
# Añadir un elemento
en_mochila.add("cuchillo")
print(en_mochila)
# Comprobar si un elemento está en el conjunto
"bocadillo" in en_mochila
"cerillas" not in en_mochila
# Quitar un elemento del conjunto
en_mochila.discard("cuerda")
print(en_mochila)

# OPERACIONES
# Unión
a = {1, 2, 3, 5, 8}
b = {1, 2, 4, 8, 16}
a.union(b)
# Elementos que están en a o en b
a | b
# Intersección
a.intersection(b)
# Elementos que están en a y en b
a & b
# Diferencia entre a y b
a.difference(b)
# Elementos que están en a pero no en b
a - b
# Diferencia simétrica
a.symmetric_difference(b)
# Elementos que están solo en a o en b
a ^ b
# Subconjunto
s = {1, 2}
s.issubset(a)
# Todos los elementos de s están en a
s <= a
# Al reves
a.issuperset(s)
a >= s

# DICCIONARIOS: CON CLAVE/VALOR INMUTABLES (NO VALEN LISTA)
# Diccionario vacío
libreta_telefonos = {}
# clave : valor
libreta_telefonos = { "Carlos" : 5556045, "Luis" : 5556048 , "Javier" : 5556051 }
# Acceder a un valor
libreta_telefonos["Luis"]
# Añadir una nueva clave : valor
libreta_telefonos["Daniel"] = 5556056
# Cambio de valor
libreta_telefonos["Carlos"] = 5556033
print(libreta_telefonos)
# Buscar una clave en el diccionario
"Luis" in libreta_telefonos
# Eliminar una pareja clave: valor
del libreta_telefonos["Luis"]
print(libreta_telefonos)
# Iterar sobre claves
for nombre in libreta_telefonos:
    print(nombre, "=", libreta_telefonos[nombre])
# Iterar sobre las parejas clave : valor
for nombre, telefono in libreta_telefonos.items():
    print(nombre, "=", telefono)
# Iterar sobre los valores
for telefono in libreta_telefonos.values():
    print(telefono)

# DEFINICIONES POR COMPRESIÓN
# Preparamos una lista vacía para ir poniendo los resultados
tabla_7 = []
# Iteramos los números del 0 al 9
for x in range(0, 10):
    tabla_7.append(7 * x)
print(tabla_7)

# Mas sencillo
tabla_7 = [ 7 * x for x in range(0, 10) ]
print(tabla_7)
# Ver si es par el multiplicador 
tabla_7_pares = [ 7 * x for x in range(0, 10) if x % 2 == 0 ]

# Ejemplo 2
lista_frutas = ["pera", "manzana", "ciruela", "cereza"]
lista_frutas =[ fruta.upper() for fruta in lista_frutas if fruta.startswith("c") ]
print(lista_frutas)

# Ejemplo 3
ejemplo3 = [ x * y for x in (1, 2, 3) for y in (4, 5, 6) ]
print(ejemplo3)

# Ejemplo 4 CONJUNTO
ejemplo4 = { x for x in range(10) if x % 2 != 0 }
print(ejemplo4)

# Ejemplo 5 TUPLA
tuple( x for x in range(5) )

# Ejemplo 6 DICCIONARIO (clave multiplicador : valor resultado)
dict_tabla_7 = { num : 7 * num for num in range(0, 10) }
print(dict_tabla_7[1])

# GENERADORES
gen_tabla_7 = ( 7 * x for x in range(0, 10) )
print(gen_tabla_7)

for v in gen_tabla_7:
    print(v)

# Extraer valores a una lista
gen_tabla_3 = ( 3 * x for x in range(0, 10) )
lista_tabla_3 = list(gen_tabla_3)
print(lista_tabla_3)