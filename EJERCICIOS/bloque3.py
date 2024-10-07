#Solicita al usuario tres números enteros y después crea una función que reciba 
#los tres números y muestre por pantalla el resultado. Puedes realizarlo en una 
#función o puedes utilizar más de una.
def tres_numeros(numero1, numero2, numero3):
    print(numero1, numero2, numero3)
print("Introduzca el primer numero")
numero1 = int(input())
print("Introduzca el segundo numero")
numero2 = int(input())
print("Introduzca el tercer numero")
numero3 = int(input())
tres_numeros(numero1,numero2,numero3)

#Crea una función que calcule la suma de una lista de números y
#muestra por pantalla el resultado.
def suma_lista_numeros(lista):
    suma = sum(lista)
    print("El resultado de sumar la lista es: ", suma)
numeros = [1, 2, 3, 6]
suma_lista_numeros(numeros)

#Crea una función que muestre los números pares de una lista de
#números y muestra el resultado por pantalla.
def numeros_pares(lista):
    pares = [num for num in lista if num % 2 == 0]
    print("Los numeros pares de la lista son: ", pares)
numeros = [2, 4, 5, 6, 7, 8]
numeros_pares(numeros)

#Crea una función que realice la suma de números de 0 a 10
def suma_numeros():
    cont = 0
    suma = 0
    while cont <= 10:
        suma = suma + cont
        cont = cont + 1
        print("El resultado de la suma es: ", suma)
suma_numeros()

#Crea una función que consulte una pregunta del usuario y que en
#función de la respuesta envíe un mensaje u otro. Si ninguna de las
#respuestas coincide con la que le proporciones al usuario en el
#mensaje entonces que se le vuelva a realizar la pregunta.
def consultar_pregunta():
    while True:
        respuesta = input("¿Te gusta programar? (Sí/No): ").lower()

        if respuesta == "sí":
            print("¡Eso es genial!")
            break
        elif respuesta == "no":
            print("Oh, ¡quizás encuentres algo más que te apasione!")
            break
        else:
            print("Respuesta no válida. Por favor, responde 'Sí' o 'No'.")
consultar_pregunta()


#Crea una función que reciba una tupla o lista de números y devuelva 
#el número de elementos inferiores a 10 que hay. Muestra el resultado 
#por pantalla.
def menores_a_diez(numeros):
    elementos_menores = [num for num in numeros if num < 10]
    print("El numero de elementos menor que diez es: ", len(elementos_menores))

lista_numeros = [5, 4, 90, 12, 10, 13, 1, 2]
menores_a_diez(lista_numeros)

#Solicita a un trabajador que indique las horas que ha trabajado y el
#precio al que le pagan la hora. Después crea una función que calcule 
#el salario del trabajador teniendo en cuenta que, si ha trabajado
#menos o igual a 35h semanales su salario será el producto de las
#horas por su precio, mientras que si ha trabajado más su salario
#será las horas por el precio más un plus de 10€ por hora. Muestra
#el resultado por pantalla.
def calcular_salario(horas_trabajadas, precio_hora):
    if horas_trabajadas <= 35:
        salario = horas_trabajadas * precio_hora
    else:
        salario = 35 * precio_hora + (horas_trabajadas - 35) * (precio_hora + 10)
    return salario
horas_trabajadas = float(input("¿Cuantas horas ha trabajado?: "))
precio_hora = float(input("¿A cuanto se le paga la hora?: "))
salario = calcular_salario(horas_trabajadas, precio_hora)
print("El salario del trabajador es: ", salario)


#Solicita al usuario que te indique cuantas noches de hotel ha reservado, 
#cuantos días del viaje a alquilado un coche y a qué ciudad ha
#viajado. Las ciudades sólo podrán ser: Alicante, Barcelona y Sevilla.
def viaje():
    noches_hotel = int(input("¿Cuantas noches de hotel ha reservado? "))
    dias_alquiler_coche = int(input("¿Cuantos dias ha alquilado un coche? "))
    ciudad = input("¿A que ciudad ha viajado?¿Alicante, Barcelona o Sevilla? ")

    ciudades_posibles = ["Alicante", "Barcelona", "Sevilla"]
    while ciudad not in ciudades_posibles:
        print("No ha ingresado una ciudad valida")
        ciudad = input("¿A que ciudad ha viajado?¿Alicante, Barcelona o Sevilla? ")
    return noches_hotel, dias_alquiler_coche, ciudad
noches, dias_alquiler, ciudad_viaje = viaje()
print("//////////VIAJE////////")
print("Noches de hotel: ", noches)
print("Dias de alquiler del coche: ", dias_alquiler)
print("Ciudad destino: ", ciudad_viaje)

#a) Crea una función que determine el coste del hotel si el precio por
#noche es de 140€
def coste_noche(noches):
    total = noches * 140
    return total
total_noches = coste_noche(noches)
print("El precio total de la estancia en el hotel es: ", total_noches)

#b) Crea una función que determine el coste del avión, si el precio del
#viaje hacia Alicante es de 250€, hacia Barcelona de 450€ y hacia Sevilla de 400€
def avion(ciudad_viaje):
    if ciudad_viaje == "Alicante":
        precio_avion = 250
    elif ciudad_viaje == "Barcelona":
        precio_avion = 450
    else:
        precio_avion = 400
    return precio_avion
total_avion = avion(ciudad_viaje)
print("El precio del avion hasta ", ciudad_viaje, " es: ", total_avion)

#c) Crea una función que determine el coste del alquiler del vehículo, si
#sabes que el precio del alquiler es de 35€ el día. Teniendo en cuanta
#que, si ha reservado el coche tres días o más, tiene un descuento en
#el precio del 5%, mientras que si lo ha reservado 7 días o más tiene
#un descuento del 20%
def alquiler_vehiculo(dias_alquiler):
    if dias_alquiler < 3:
        precio_alquiler = dias_alquiler * 35
    elif 3<= dias_alquiler < 7:
        precio_alquiler = (dias_alquiler * 35) * 0.95
    elif dias_alquiler >=7:
        precio_alquiler = (dias_alquiler * 35) * 0.80
    return precio_alquiler
total_vehiculo = alquiler_vehiculo(dias_alquiler)
print("Lo que cuesta el alquiler del vehiculo por ", dias_alquiler, " dias es: ", total_vehiculo)

#d) Crea una función que reciba todos los parámetros anteriores y
#muestre por pantalla el importe que le ha costado el viaje.
def importe_total(total_noches, total_avion, total_vehiculo):
    total_viaje = total_noches + total_avion + total_vehiculo
    return total_viaje
precio_viaje_completo = importe_total(total_noches, total_avion, total_vehiculo)
print("El precio tottal del viaje es: ", precio_viaje_completo)


