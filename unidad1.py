#Definir una variable
mensaje = "Hola Mundo!"
#Imprimir la variable
print(mensaje)

#OTROS EJEMPLOS
nombre = "Papu"
nombre_completo = "Cinthya Perez"
edad_jugador = 20
#Asignación multiple, mismo valor, dos variables
goles_marcados = goles_fallados = 0
#Asignacion simultanea, valores idstintos a cada variable
tarjetas_amarillas, tarjetas_rojas = 1,0

#Cambio de valores
x = 10
y = 20
print("x = ", x, "y = ", y)
x, y = y, x
print("x = ", x, "y = ", y)

#NO EXISTEN LAS CONSTANTES
VERSION = "1.0"
PI = 3.14159265359

#Operaciones
suma = 3 + 5
resta = 5 - 3
multiplicacion = 3 * 4
suma_fn = 3 + 5.5
resta_fn = 5.5 - 3
multiplicacion_fn = 3.0 * 4
division = 6 / 3
dicision2 = 13 / 2
division_entera = 13 // 2
modulo = 13 % 2
potencia = 3 ** 2
valor_absoluto = abs(-3)
redondear = round(2/3, 1) #una cifra decimal
redondear2 = round(2/3, 2)

#Cadena de caracteres (son inmutables)
#Comillas simples
texto_1 = 'Cadena de texto'
#Comillas dobles
texto_2 = "Cadena de texto"
#Comillas simples dentro de comillas dobles
texto_3 = "Cadena 'de' texto"
#Comillas dobles dentro de comillas simples
texto_4 = 'Cadena "de" texto'
#texto varias lineas
texto_multiple_1 = """lorem ipsum"""
texto_multiple_2 = '''lorem upsum'''
#Combinar texto
lenguaje = 'Py' + 'thon'
lenguaje + "esco"
#repetir una cadena varias veces
"hola" * 3
#Longitud
print(lenguaje)
print(len(lenguaje))
#seleccionar un caracter
lenguaje[0]
#ultimo caracter
lenguaje[len(lenguaje) - 1]
lenguaje[-1]
#seleccionar una rebana
lenguaje[2:6]
lenguaje[2:]
lenguaje[-2:]
lenguaje[:-2]
lenguaje[:2] + lenguaje[2:]
#MANUPULAR CADENAS DE TEXTO
#Mayusculas
lenguaje.upper()
#Minusculas
lenguaje.lower()
#Conar veces que aparece un aletra en la cadena
lenguaje.count('o')
#Remplazar un caracter por otro
lenguaje.replace('p',  'c')
#Trocear
autor = "Jacinto Benavente"
autor.split(' ')
#Trocear y guardar en variables
nombre, apellido = autor.split()
print(nombre)
print(apellido)
#Seleccionar el sepador
";;;".join([apellido, nombre])
#Comprobar si esta compuesta por letras
"abc".isalpha()
#Comprobar si esta compuesta por numeros
"123".isdigit()
#Formatear insertando valores donde {}
"{} gano el premio Nobel en {}".format(autor, 1922)
#Mas operaciones
help(str)

#BOOLEANOS
soy_rico = False
soy_listo = True
#AND (Y)
soy_rico and soy_listo
#OR (O)
soy_rico or soy_listo
#Negacion
not soy_rico
#Operadores de comparacion
10 > 3.0
10 < 3.0
10 >= 3.0
10 <= 3.0
6/3 == 2
"Rojo" != "Verde"
#None
voluntario = None
voluntario is None