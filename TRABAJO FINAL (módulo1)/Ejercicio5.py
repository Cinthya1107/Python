import random
#definir una tupla compuesta por 15 números enteros positivos aleatorios entre 0 y 100
loteria_ganadores = tuple(random.randint(0, 100) for _ in range(15))

#se asegura de que el numero introducido sea positivo
def obtener_numero():
    while True:
        try:
            numero = int(input("Por favor, introduzca un número entero positivo: "))
            if numero < 0:
                print("El número debe ser positivo. Por favor, inténtelo de nuevo.")
                continue
            return numero
        except ValueError:
            print("Debe introducir un número entero. Por favor, inténtelo de nuevo.")
            
#solicitar al usuario que introduzca su número
numero_usuario = obtener_numero()

#mostrar la lista de números ganadores
print("Números ganadores del último sorteo de la lotería:")
print(loteria_ganadores)

#encontrar y mostrar el número más pequeño y el más grande
minimo = min(loteria_ganadores)
maximo = max(loteria_ganadores)
print(f"Número ganador más pequeño: {minimo}")
print(f"Número ganador más grande: {maximo}")

# Comprobar si el número del usuario está en la lista de ganadores
if numero_usuario in loteria_ganadores:
    veces_repetido = loteria_ganadores.count(numero_usuario) #calcula las veces que se ha repetido el número
    premio = 15 + (veces_repetido - 1) * 5 #calcula el premio segun las veces que se repitió el número
    if veces_repetido == 1:
        print(f"¡Felicidades! Su número: {numero_usuario} se encuentra dentro de la lista de ganadores. Ha ganado un total de {premio}€")
    else:
        print(f"¡Felicidades! Su número: {numero_usuario} se encuentra dentro de la lista de ganadores y además se ha repetido {veces_repetido} veces. Ha ganado un total de {premio}€")
else: #el numero no coincide
    respuesta = input("Lo sentimos. Su número no ha resultado premiado. ¿Desea volver a intentarlo? (SI/NO): ").upper() #pregunta al usuario si quiere seguir jugando
    while respuesta not in ("SI", "NO"):
        respuesta = input("No hemos logrado entender su respuesta. Repítala, por favor. ¿Desea volver a intentarlo? (SI/NO): ").upper() #una respuesta no esperada
    if respuesta == "SI": #sigue jugando
        numero_usuario = obtener_numero() #llama a la función que comprueba el número
        if numero_usuario in loteria_ganadores:
            veces_repetido = loteria_ganadores.count(numero_usuario)
            premio = 15 + (veces_repetido - 1) * 5
            if veces_repetido == 1:
                print(f"¡Felicidades! Su número: {numero_usuario} se encuentra dentro de la lista de ganadores. Ha ganado un total de {premio}€")
            else:
                print(f"¡Felicidades! Su número: {numero_usuario} se encuentra dentro de la lista de ganadores y además se ha repetido {veces_repetido} veces. Ha ganado un total de {premio}€")
        else:
            print("Lo sentimos. Su número no ha resultado premiado. El programa finalizará.")
    else:
        print("El programa finalizará.")
