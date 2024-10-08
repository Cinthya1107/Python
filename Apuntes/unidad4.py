#ENTRADA Y SALIDA DE DATOS
import os
#Ajustamos el directorio
DIR_U09_AUX = os.path.join(".", "U09_aux")
nombre_fichero = os.path.join(DIR_U09_AUX, "lorem_ipsum.txt")

#abrimos el fichero de texto (lectura)
f = open(nombre_fichero, "r")
#leemos la primera linea
linea_1 = f.readline()
print(linea_1)
#leer varias lineas
"""lineas = f.readlines() #devuelva una lista
print(lineas)"""
#es mejor iterar para todas las lineas
for linea in f:
    print(linea)
#cerramos el fichero
f.close()

#Leemos y escribimos sobre un fichero
f_in = open(nombre_fichero, "r")
f_out = open("resultado.txt", "w")
#iteramos sobre el fichero de entrada
for linea in f_in:
    palabras = linea.split() #dividimos el texto el palabras
    n_palabras = len(palabras) #las contamos
    f_out.write(str(n_palabras)) #escribimos el numero de palabras en el fichero nuevo
    f_out.write("\n") #ponemos el final de linea

f_in.close()
f_out.close()

#posicionarse en un fichero
f = open(nombre_fichero, "r")
pos_0 = f.tell()
print("Posicion inicial:", pos_0)

linea_1 = f.readline()
pos_1 = f.tell()
print("Linea 1:", linea_1)
print("Tras leer linea 1, pos:", pos_1)

linea_2 = f.readline()
pos_2 = f.tell()
print("Linea 2:", linea_2)
print("Tras leer linea 2, pos:", pos_2)

#Volver a la posicion 0
f.seek(0)
print("Volvemos al inicio del fichero")

#Nos movemos a la posicion 2
f.seek(pos_2)
print("saltamos a la linea 2")
linea_3 = f.readline()
pos_3 = f.tell()
print("Linea 3", linea_3)
print("Tras leer linea 3, pos", pos_3)

f.close()

#Cerrar automaticamente el fichero
with open(nombre_fichero, "r") as f:
    #podemos hacer cualquier proceso de los de antes
    for linea in f:
        linea = f.readline()
        print(linea)
print("¿El fichero esta cerrado?", f.closed)

#SYS, archivo loop_lee_stdin.py

#OBJETOS
#clase
class Coche:
    #atributo
    ruedas = 4
    #constructor
    def __init__(self, potencia, velocidad_max, color):
        self.potencia = potencia
        self.velocidad_max = velocidad_max
        self.color = color
        self.velocidad = 0
    #metodos de la clase
    def acelera(self, incremento):
        self.velocidad = self.velocidad + incremento
        if(self.velocidad > self.velocidad_max):
            print("Voy a todo gas!!!")
            self.velocidad = self.velocidad_max
        else:
            print("Voy a %d" % self.velocidad)
    def comprueba_coche():
        print("Soy un coche")

#Herencia
class Familiar(Coche):
    def __init__(self, potencia, velocidad_max, color, maletero):
        super().__init__(potencia, velocidad_max, color)
        self.maletero = maletero
        self.carga = 0

    def pon_carga(self, peso):
        self.carga = self.carga + peso
        if(self.carga > self.maletero):
            print("No cabe mas !!!")
            self.carga = self.maletero
        else:
            print("llevo %d kg" % self.carga)
    #Poliformismo
    def acelera(self, incremento):
        self.velocidad = self.velocidad + 0.5 * incremento
        if(self.velocidad > 120):
            print("A donda vas??!!!")
            self.velocidad = self.velocidad_max
        else:
            print("He subido solo a %d" % self.velocidad)

#Objetos
print(Coche.ruedas)
Coche.comprueba_coche()
#c1 = Coche()
coche_1 = Coche(120, 200, "rojo")
coche_2 = Coche(150, 220, "azul")
#print(c1)
print(coche_1.color)
print(coche_2.color)
#asociando valores al metodo acelera
coche_1.acelera(50)
coche_1.acelera(60)
coche_1.acelera(100)
#clase "familiar" herenccia
fam_1 = Familiar(130, 180, 'gris', 300)
print(fam_1)
fam_1.acelera(40)
fam_1.pon_carga(50)
fam_1.pon_carga(500)
#clase "familiar" poliformismo
fam_2 = Familiar(120, 180, "negro", 250)
fam_2.acelera(70)
fam_2.acelera(80)
fam_2.acelera(100)
