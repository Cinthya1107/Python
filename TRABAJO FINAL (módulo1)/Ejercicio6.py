#Ejercicio 6: agenda para almacenar contactos que no guarde nombre repetidos
#diccionario vacio que alamacenará los contactos
agenda = {}

#Función que se encarga de agregar los contactos
def agregar_contacto(): 
    nombre = input("Por favor, introduzca el nombre del contacto: ") #pide al usuario el nombre del contacto y lo almacena
    if nombre in agenda: #si el contacto existe
        print("El nombre ya existe en la agenda. Por favor, inténtelo de nuevo.")
        return
    telefono = input("Por favor, introduzca el número de teléfono del contacto: ")#pide al usuario el número del contacto y lo almacena
    agenda[nombre] = telefono #introduce la clave:valor (nombre:teléfono)
    print("Contacto agregado correctamente.")

#Funcion que itera entre el diccionario de la agenda
def mostrar_agenda():
    print("Agenda de contactos:")
    for nombre, telefono in agenda.items(): #itera y muestra los contactos (clave:valor)
        print(f"Nombre: {nombre}, Teléfono: {telefono}")

while True: #pregunta si quiere añadir mas contactos
    agregar_contacto()
    respuesta = input("¿Desea agregar otro contacto? (SI/NO): ").upper()
    while respuesta not in ("SI", "NO"): #si la respuesta no es una de las dos esperadas
        respuesta = input("No hemos entendido su respuesta. Por favor, repítala. ¿Desea agregar otro contacto? (SI/NO): ").upper()
    if respuesta == "NO": #si no desea guardar mas contactos
        mostrar_agenda()
        print("El programa ha finalizado.")
        break
