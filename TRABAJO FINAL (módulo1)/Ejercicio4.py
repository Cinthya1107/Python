#Ejercicio 4: Objeto clase italiano, con datos introducidos por el usuario, y el metodo saludo con un objeto italiano
class Persona:
    def __init__(self, nombre, apellido, nacionalidad):
        self.nombre = nombre
        self.apellido = apellido
        self.nacionalidad = nacionalidad
    def saludo(self, nombre, apellido):
        print("Hola, mi nombre completo es", nombre, apellido)

class Italiano(Persona):
    def __init__(self, nombre, apellido):
        super().__init__(nombre, apellido, "Italiana")
        self.idioma = "Italiano"

    def saludo(self):
        print("Bonjorno! Mi nombre es: {} {} , soy de nacionalidad italiana y mi idioma principal es italiano.".format(self.nombre, self.apellido))

def crear_objeto():
    objeto_nombre = input("Por favor introduca el nombre")
    objeto_apellido = input("Por favor introduca el apellido")
    persona = Italiano(objeto_nombre, objeto_apellido)
    persona.saludo()

crear_objeto()


