import random
import collections
# Crea un programa que obtenga un número aleatorio del 0 al 100 y
# muéstralo por pantalla.
for i in range(1):
    print(random.randrange(0, 100, 1))
# Solicita al usuario que escriba su nombre y muéstralo por pantalla
print("Introduzca su nombre")
nombre = input()
print("Te llamas {}".format(nombre))
# Crea un programa que obtenga un número aleatorio y le solicite al
# usuario un número para ver si coinciden. 
numero_generado = random.randrange(0, 11, 1)
#print(numero_generado)

print("Introduzca un munero")
numero_ingresado = input()
numero_ingresado = int(numero_ingresado)
if numero_ingresado != numero_generado:
    print("No son el mismo numero")
else:
    print("Son el mismo numero")
# Crea una lista de números y muéstralos por pantalla
lista_nums = [1, 6, 2, 5, 3, 4]
print(lista_nums)
# Crea una lista de strings (cadenas de caracteres) y ordena sus elementos en función de su 
# número de caracteres. Muestra por pantalla el resultado.
lista_string = ["abeja", "caracola", "zorro", "pepino", "diana"]
lista_string.sort()
print(lista_string)
# Crea una tupla de strings y muéstrala por pantalla. 
palos_baraja = ("corazones","diamantes","tréboles","picas")
print(palos_baraja)
# Crea una tupla de elementos de diferentes tipos y muestra el resultado por pantalla.
tupla_ejemplo = ("A", 1, 2.3, "cochinillos", True)
print(tupla_ejemplo)
# Crea una tupla de elementos de diferentes tipos, luego añade un
# elemento más y muestra el resultado por pantalla. Puedes utilizar
# conversión de datos para realizar este ejercicio.
tupla_ejemplo1 = ("A", 1, 2.3, "cochinillos")
lista = list(tupla_ejemplo1)
lista.insert(1, 20)
tupla_ejemplo1 = tuple(lista)
print(tupla_ejemplo1)
# Crea una tupla y conviértela en un String. Muestra el resultado por pantalla.
tupla_ejemplo2 = ("A", 1, 2.3, "cochinillos", False)
tupla_string = str(tupla_ejemplo2)
print(tupla_string)
# Crea una tupla y cuenta cuantas veces se repite un número de la
# tupla. Muestra el resultado por pantalla
tupla_ejemplo3 = (1, 3, 54, 1, 25, 3)
print(tupla_ejemplo3.count(1))
# /////////// Otra manera de hacerlo //////////////
cantidad = collections.Counter(tupla_ejemplo3)
print(cantidad)
# Crea una tupla en la que todos sus elementos sean letras y averigua si una determinada 
# letra existe en la tupla o no. Muestra el resultado por pantalla.
tupla_ejemplo4 = ("A", "B", "J", "L")
print("Introduce una letra en mayúsculas")
letra = input()
for caracter in tupla_ejemplo4:
    if letra == caracter:
        print("La letra introducida pertenece a la tupla")
        break
    else:
        print("La letra introdcida no pertenece a la tupla")
        break
# Crea una tupla y comprueba su longitud. Muestra el resultado por pantalla.
tupla_ejemplo5 = (1, 2, 3, 4, 5, 6)
print(len(tupla_ejemplo5))
# Crea una lista de cinco elementos y crea un bucle que muestre su
# contenido. Muestra el resultado por pantalla.
tupla_ejemplo6 = (1, 2, 3, 4, 5)
for i in tupla_ejemplo6:
    print(i)
# Genera una secuencia de números del 0 al 10, que se incremente
# de 1 en 1 y muéstralo por pantalla. Repite el ejercicio, pero ahora
# haciendo que se incrementen de 2 en 2
for i in range(11):
    print(i)

print("De dos en dos")

for j in range (0, 11, 2):
    print(j)
# Crea un programa que cuente los números pares e impares de una
# tupla de números del 0 al 10 y muestra el resultado por pantalla
tupla_ejemplo7 = ()
for i in range(11):
    print(i)
    tupla_ejemplo7 += (i,)
print(tupla_ejemplo7)
# Crea una lista de elementos de diferente tipo, después haz un bucle que muestre 
# cada dato y su tipo por pantalla.
lista_dif_datos = [1, "A", False]
for i in lista_dif_datos:
    print("Dato: ", i, " Tipo de dato: ", type(i))
# Crea un diccionario y realiza un bucle que muestre por pantalla cada clave del diccionario. 
# Repite el ejercicio creando un bucle que
# muestre por pantalla los valores de las claves.
diccionario = {
    "nombre": "Cinthya",
    "edad": 20,
    "genero": "Femenino"
}
print("CLAVES")

for clave in diccionario:
    print(clave)

print("VALORES")
for clave, valor in diccionario.items():
    print(valor) 
# Crea un bucle que permita imprimir números desde 0 mientras estos no lleguen a 10. 
# Crea además un bucle que permita contar desde 0 mientras los números no lleguen a 10 y que 
# realice la suma de los números contados. Muestra los resultados por pantalla.
print("Primer bucle")
for numero in range(10):
    print(numero)

print("Segundo bucle")
suma_numeros = 0
for numero in range(10):
    print(numero)
    suma_numeros += numero
print("La suma es: ", suma_numeros)
# Crea un diccionario llamado menú dónde guardes el nombre de un
# alimento y su precio. Después crea un bucle que permita solicitar
# al usuario un alimento y le informe del total del pedido hasta que
# el usuario ya no quiera pedir más y entonces se le informe del total
# de la cuenta. El usuario saldrá del bucle si no introduce ningún dato. 
# Si introduce un alimento que se encuentre fuera del menú se le
# informará que no disponemos de dicho alimento en el menú.
menu = {"filipinos": 1.40}
pedido = {}
cuenta = 0.0

while True:
    print("Introduzca un alimento")
    alimento = input()
   
    if alimento == 'SALIR':
        break

    if not alimento:
        break

    if alimento in menu:
        print("¿Cuanta cantidad desea?")
        cantidad = int(input())

        pedido[alimento] = cantidad
        cuenta += menu[alimento] * cantidad
        print(cuenta)

    else:
        print("No disponemos de ese alimento")
print("Si no quiere seguir comprando ponga: 'SALIR' ")
# Crea una lista de números y averigua el más mayor y el más pequeño. 
# Luego muéstralos por pantalla.
lista_numeros = [1, 2, 3, 4, 20, 10]
numero_mayor = max(lista_numeros)
numero_menor = min(lista_numeros)
print("Adivina el numero mayor")
mayor = int(input())
print("Adivina el numero menor")
menor = int(input())
if numero_mayor == mayor and numero_menor == menor:
    print("Has acertado el numero mayor y el menor")
elif numero_mayor == mayor and numero_menor != menor:
    print("Has acertado el numero mayor y pero no el menor")
elif numero_mayor != mayor and numero_menor == menor:
    print("No has acertado el numero mayor y pero si el menor")
else:
    print("No has acertado ninguno de los números")

    
