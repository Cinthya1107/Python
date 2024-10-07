#ENTRADA Y SALIDA DE DATOS 
import os
DIR_U09 = os.path.join(".", "U09_aux")
nombre_fichero = os.path.join(DIR_U09, "lorem_ipsum.txt")
f = open(nombre_fichero, "r")
linea_1 = f.readline()
print(linea_1)
f.close

#Que devuelva todo el texto en forma de lista
f = open(nombre_fichero, "r")
lineas = f.readlines()
print(lineas)
f.close()
#Una forma mas eficiente y practica
f = open(nombre_fichero, "r")
for linea in f:
    print(linea)
f.close()

#ESCRIBIR EN FICHEROS
f_in = open(nombre_fichero, "r")
f_out = open("resultado.txt", "w")
for linea in f_in:
    palabras = linea.split()
    n_palabras = len(palabras)
    f_out.write(str(n_palabras))
    f_out.write("")
f_in.close()
f_out.close()

#MOVERNOS POR EL FICHERO
#El principio del fichero
f = open(nombre_fichero, "r")
pos_0 = f.tell()
print("Posicion inicial:", pos_0)
#La primera linea del fichero
linea_1 = f.readline()
pos_1 = f.tell()
print("Linea 1: ", linea_1)
print("Tras leer la linea 1, pos:", pos_1)
#La segunda linea del fichero
linea_2 = f.readline()
pos_2 = f.tell()
print("Linea 2: ", linea_2)
print("Tras leer la linea 2, pos:", pos_2)
#Nos volvemos a colocar al inicio del fichero
f.seek(0)
print("Volvemos al inicio del fichero")
#Leemos la tercera linea saltando hasta la segunda
f.seek(pos_2)
print("salatamos hasta la linea 2 y leemos la 3")
linea_3 = f.readline()
pos_3 = f.tell()
print("La tercera linea es: ", linea_3)
print("Y nos encontramos en la posicion:", pos_3)
f.close()
#Forma alternativa que cierra el archivo automaticamente
with open(nombre_fichero, "r") as f:
    for linea in f:
        print(linea)
print("¿El fichero esta cerrado?", f.closed)

#ENTRADA Y SALIDA ESTANDAR 
"""import sys
sys.stdout.write("Prueba a escribir (la linea vacia sirve para salir)")
while True:
    x = sys.stdin.readline()
    if (len(x) > 0) and (x != " ") and (x !=' '):
        mensaje = "He leido {}".format(x)
        sys.stdout.write(mensaje)
    else:
        sys.stderr.write("No hay mas datos")
        break"""

#CLASES Y PROGRAMACION ORIENTADA A OBJETOS
#Definir clases y objetos
class Coche:
    ruedas = 4
    #Constructores
    def __init__(self, potencia, velocidad_max, color):
        self.potencia = potencia
        self.velocidad_max = velocidad_max
        self.color = color
        self.velocidad = 0
    #Metodos
    def acelera(self, incremento):
        self.velocidad = self.velocidad + incremento
        if(self.velocidad > self.velocidad_max):
            print("Voy a todo gas!!!")
        else:
            print("Voy a %d" % self.velocidad)
    #Metodo de clase
    def comprueba_coche():
        print("Soy un coche")

print(Coche.ruedas)
mi_coche = Coche(100,2000, "Verde")
mi_coche.acelera(5)
print(mi_coche)
print(mi_coche.potencia, mi_coche.velocidad_max, mi_coche.color)

#Herencia
class Familiar(Coche):
    def __init__(self, potencia, velocidad_max, color, maletero):
        super().__init__(potencia, velocidad_max, color)
        self.maletero = maletero
        self.carga = 0
    def po_carga(self, peso):
        self.carga = self.carga + peso
        if(self.carga > self.maletero):
            print("No cabe nada masss!!!")
        else:
            print("Llevo %d kg" % self.carga)
    #Poliformismo
    def acelera(self, incremento):
        self.velocidad = self.velocidad + incremento
        if(self.velocidad > 120):
            print("Te vas a estrellarrr!!!!")
            self.velocidad = self.velocidad_max
        else:
            print("He subido solo a %d" % self.velocidad)
        
fam_1 = Familiar(130, 180, "gris", 300)
print(fam_1)
fam_1.acelera(40)
fam_1.po_carga(50)
fam_1.acelera(140)