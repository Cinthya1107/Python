#Ejercicio 2: guardar alumnos y sus notas en distintas materias e imprimir:
"""
Cuantos alumnos suspendieron cada asignatura
Las notas media de cada alumno
Cuantos alumnos han superado el curso (media >= 5)
"""
#Guardamos los datos en un diccionario
latin = {"alumno_1" : 8,"alumno_2" : 7, "alumno_3" : 10, "alumno_4" : 4, "alumno_5" : 9 }
castellano = {"alumno_1" : 8, "alumno_2" : 6, "alumno_3" : 7, "alumno_4" : 4, "alumno_5" : 8}
frances = {"alumno_1" : 9, "alumno_2" : 7, "alumno_3" : 8, "alumno_4" : 3, "alumno_5" : 9}
ingles = {"alumno_1" : 4, "alumno_2" : 2, "alumno_3" : 9, "alumno_4" : 2, "alumno_5" : 6}

#Cuantos alumnos han suspendido cada asigantura
def alumnos_suspensos(latin, castellano, frances, ingles):
    suspensos = 0
    
    for notas in latin.values(): #Iteramos en el diccionario "latin"
        if(notas < 5): 
            suspensos += 1 #sumamos uno a la variable suspensos si el alumno ha sacado menos de un 5
    print("Latin han suspendido ", suspensos)
    suspensos = 0 #Reseteamos la variable para que no se sumen entre asignaturas

    for notas in castellano.values():
        if(notas < 5):
            suspensos += 1
    print("Castellano han suspendido ", suspensos)
    suspensos = 0

    for notas in frances.values():
        if(notas < 5):
            suspensos += 1
    print("Frances han suspendido ", suspensos)
    suspensos = 0

    for notas in ingles.values():
        if(notas < 5):
            suspensos += 1
    print("Ingles han suspendido ", suspensos)

#Media de cada alumno
def media_notas(latin, castellano, frances, ingles):
    medias_alumnos = {} #Crea un diccionario para almacenar los datos
    for alumno in latin.keys(): #Iteramos sobre cada alumno
        media = (latin[alumno] + castellano[alumno] + frances[alumno] + ingles[alumno]) / 4 #Calculamos la media de notas de cada alumno en las asignaturas
        medias_alumnos[alumno] = media #Almacenamos esa media
        print("El {}, tiene como media {}".format(alumno, media))
    alumnos_media_superior_a_cinco(media, medias_alumnos) #Pasamos la media a otra funcion para saber si está aprobada

def alumnos_media_superior_a_cinco(media, medias_alumnos):
    # Imprimir los alumnos con media superior a 5
    for alumno, media in medias_alumnos.items(): #Itera sobre cada alumno y su media
        if media > 5: #Verifica que esa media es mayor a 5
            print(f"{alumno} tiene una media superior a 5 (Media: {media})")

# Llamar a las funciones, pasandolas los diccionarios creados
alumnos_suspensos(latin, castellano, frances, ingles)
media_notas(latin, castellano, frances, ingles)







        
