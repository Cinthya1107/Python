
#Ejercicio 1: Programa que solicite al usuario introducir un número entero positivo y almacenarlo en una variable

#Función para comprobar que es un número
def es_numero(valor):
    if valor.isalpha():
        print("El valor introducido no es un numero, introduzca un numero por favor") 
        return False
    return True

#Función que comprueba que el número introducido sea entero y positivo
def es_entero_positivo (valor):
    try: #Uso un try-except para manejar la excepción en caso de que el usuario introduzca un número decimal con comas
        numero = float(valor) #convierto el número introducido en float para comprobaciones
        if numero <= 0: #Si es menor que cero
            print("El valor introducido no es un numero positivo, introduzca un numero entero positivo por favor")
            return False
        
        if numero != int(numero): #Si no es entero (al haberlo convertido en float, ambos valores no deben coincidir)
            print("El numero introducido no es entero, vuelvalo a intentar")
            return False
        return True
    except ValueError:
        print("El numero introducido no es entero, vuelvalo a intentar")
        return False

#Función para calcular si el valor es primo
def primo(valor):
    for i in range(2, int(valor**0.5 + 1)):
        if valor % i == 0:
            return print("No es primo")
    return print("Es primo")

#Bucle para que el usuario introduzca valores hasta que se introduzca uno valido
while True:
    valor = input("Por favor introduzca un numero") #El valor introducido lo guardo en una variable
    if (es_numero(valor) and es_entero_positivo(valor)): #Si se cumplen las funciones de comprobación
        primo(int(valor)) #Se comprueba que el número sea primo, pasandolo a entero el string recibido
        break
