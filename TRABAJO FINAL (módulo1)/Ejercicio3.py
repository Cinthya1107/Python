#Ejercicio 3: dos dados simultanamente y si coincide alguno de los numeros entre si gana Jugador1
import random

#Funcion que determina el bucle del juego
def retry():
    respuesta = input("Por favor, responde con NO o SI: ")# El jugador introduce SI (seguir jugando), NO (parar)
    while True:
        if respuesta == "SI": 
            print("El usuario ha respondido SI.")
            return True #seguimos jugando
        elif respuesta.upper() == "NO":
            print("El usuario ha respondido NO.")
            return False #se para el juego
        else:
            print("Respuesta inválida. Por favor, responde con NO o SI: ")
            return False #la respuesta no es valida

puntos_2 = 0
puntos_1 = 0 
while True: #mientras la respuesta sea SI
    #generamos 4 valores aleatorios
    numero_1 = random.randint(1, 6)
    numero_2 = random.randint(1, 6)
    numero_3 = random.randint(1, 6)
    numero_4 = random.randint(1, 6)
    #imprimimos los valores que han obtenido cada jugador
    print("El jugador 1 ha obtenido: {} y {}".format(numero_1, numero_2))
    print("El jugador 2 ha obtenido: {} y {}".format(numero_3, numero_4))
    
    #si alguno de los numeros coincide
    if numero_1 == numero_2 or numero_1 == numero_3 or numero_1 == numero_4 or numero_2 == numero_3 or numero_2 == numero_4 or numero_3 == numero_4:
        print("Gana el Jugador1")
        puntos_1 +=1 #gana un punto el Jugador1
        print(puntos_1)
       
    else: #si no coincide
        print("Gana el Jugador2")
        puntos_2 +=1 #gana puntos el Jugador2
        print(puntos_2)
        
    if puntos_1 == 3: #si el Jugador1, llega a 3 puntos, gana
        print("Enorabuena Jugador1, has ganado !!!")
        print("Desea jugar otra partida?")
        if not retry(): #si el usuario no introduce "SI", el juego se acaba
            print("Gracias por jugar. ¡Hasta luego!")
            break 
        
    if puntos_2 == 3:#si el Jugador2, llega a 3 puntos, gana
        print("Enorabuena Jugador2, has ganado !!!")
        print("Desea jugar otra partida?")
        if not retry():
            print("Gracias por jugar. ¡Hasta luego!")
            break #se acaba el juego
        
   
        


