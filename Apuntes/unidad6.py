#PANDAS
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
#Creamos uuna serie
s1 = Series([3,5,7,9])
print(s1)
#serie de temperaturas anuales
temp_anual = Series([16.6, 16.2, 15.5, 17.0, 16.6, 16.5], index = [2011, 2012, 2013, 2014, 2015, 2016])
print(temp_anual)
#serie de temperaturas mensuales
temp_mensual = Series([7.2, 7.3, 12.1, 15.7, 20.3, 24.8, 28.2, 25.6, 20.8, 16.8, 12.3, 7.8], index = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Nomviembre", "Diciembre"])
print(temp_mensual)
#seleccionar elementos
s1 = Series([3, 5, 7, 9])
print(s1[2])
#seleccionar una rebanada
print(s1[1:3])
#mascara booleana
s1[s1 < 6]
#seleccionar un valor por el indice
print(temp_mensual["Enero"])
#seleccionar una lista de etiquetas/indices
temp_mensual[["Marzo", "Abril", "Mayo"]]
#operaciones matematicas
print(s1 * 2)
#operaciones elemento a elemento entre series
s2 = Series([2,3,4,5])
print(s1 - s2)
#suma de elementos
s1.sum()
#producto de elementos
s2.prod()

#DATAFRAMES 
#Con columns indicamos el orden
df1 = DataFrame({'mes' : ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Nomviembre", "Diciembre"],
                 'temp_c' :[7.2, 7.3, 12.1, 15.7, 20.3, 24.8, 28.2, 25.6, 20.8, 16.8, 12.3, 7.8],
                 'lluvia_mm' : [21, 22, 19, 39, 44, 26, 17, 17, 30, 36, 30, 21],
                 'humedad' : [75, 67, 59, 57, 54, 49, 47, 51, 57, 67, 73, 76]},
                columns = ['mes', 'temp_c', 'lluvia_mm', 'humedad'])
print(df1)
#Usar un array para algun array
df2 = DataFrame({'mes' : ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Nomviembre", "Diciembre"],
                 'imes' : np.arange(1, 13),
                 'temp_c' :[7.2, 7.3, 12.1, 15.7, 20.3, 24.8, 28.2, 25.6, 20.8, 16.8, 12.3, 7.8],
                 'lluvia_mm' : [21, 22, 19, 39, 44, 26, 17, 17, 30, 36, 30, 21],
                 'humedad' : [75, 67, 59, 57, 54, 49, 47, 51, 57, 67, 73, 76]},
                columns = ['mes', 'imes', 'temp_c', 'lluvia_mm', 'humedad'])
print(df2)
#Definir indice en DataFrame
df3 = DataFrame({'imes' : np.arange(1, 13),
                 'temp_c' :temp_mensual,
                 'lluvia_mm' : [21, 22, 19, 39, 44, 26, 17, 17, 30, 36, 30, 21],
                 'humedad' : [75, 67, 59, 57, 54, 49, 47, 51, 57, 67, 73, 76]},
                columns = ['mes', 'imes', 'temp_c', 'lluvia_mm', 'humedad'],
                index = ["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"])
print(df3)
print(df3.index)
#columnas de DataFrame
df3.columns
#tamaño del DataFrame
df3.shape
#sacar el numero de filas
df3.shape[0]
#tamaño total (num. total del elementos)
df3.size
#mostrar primers filas
df3.head()
#o de las ultimas
df3.tail(3)
#contar los elementos no nulos
df3.count()
#estadisticas basicas de cada columna
df3.describe()
#seleccionar por nombre
df_meteo = DataFrame({'imes' : np.arange(1, 13),
                 'temp_c' :temp_mensual,
                 'lluvia_mm' : [21, 22, 19, 39, 44, 26, 17, 17, 30, 36, 30, 21],
                 'humedad' : [75, 67, 59, 57, 54, 49, 47, 51, 57, 67, 73, 76]},
                columns = ['mes', 'imes', 'temp_c', 'lluvia_mm', 'humedad'],
                index = ["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"])
df_meteo["lluvia_mm"]
#acceder a una columna
df_meteo.temp_c
#si el nombre de una columna coincide con el de un atributo, se muestra el atributo
df_geom = DataFrame({
    'shape' : ["triangle", "square", "circle"],
    'area' : ["b*h/2", "a*a", "PI*r*r"]
})
df_geom["shape"]
#numero de filas y columnas
df_geom.shape
#acceder a columnas
df_meteo[["imes", "temp_c"]]
#indicamos una rebana de indices
df_meteo[0:4]
#rebana de etiquetas
df_meteo["Ene":"Mar"]
#seleccionar filas con condiciones
df_meteo[df_meteo.temp_c > 20.0] #la temperatura supere 20 grados
#Etiquetas df.loc
#elemento concreto ([fila, columna])
df_meteo.loc["May", "lluvia_mm"]
#seleccionar una fila entera
df_meteo.loc["May", ]
#seleccionar una columna entera
df_meteo.loc[:, "humedad"]
#subconjunto de filas y columnas
df_meteo.loc["Feb":"Abr", ["lluvia_mm", "humedad"]]
#selccionar un elemento concreto
df_meteo.iloc[6, 2]
#seleccionar una fila entera
df_meteo.iloc[6, ]
#seleccionar una columna entera
df_meteo.iloc[:, 1]
#seleccionar un subjunto de filas y columnas
df_meteo.iloc[0:3, 1:3]
#mascaras booleanas
df_meteo.loc["Jun" : "Ago", "temp_c"] = df_meteo.loc["Jun" : "Ago", "temp_c"] + 1
print(df_meteo)
#añadir una columna, con mismo valor para todas las filas
df_meteo["limite_temp_c"] = 50
#dando valores individuales a cada elemento
#pasar los grados a Fahrenheit
df_meteo["temp_F"] = 1.8 * df_meteo["temp_c"] + 32
print(df_meteo)
#Trabajando con datos en fichero
#leyendo datos de fichero
df_flights = pd.read_csv("./U09_datasets/NYC_flights_2013_MINI.csv", sep = ";")
df_flights.shape
#mostramos las primeras filas y columnas del DataFrame
df_flights.iloc[0:5, 0:10]
#escribir datos
df_mini = df_flights.head()
#guardamos en fichero (salvar el contenido)
df_mini.to_csv("./Prueba_export_panda.csv", sep = ";", na_rep = "", header = True, index = False, index_label = False)
#emparejas los elementos de ambas variables (mismo indice)
fruta_kg = Series({'peras' : 2, 'manzanas' : 1, 'naranjas' : 3})
fruta_precio = Series({'manzanas' : 1.95, 'naranja' : 1.90, 'peras' : 1.50, 'uva' : 2.60})
#multiplicamos
fruta_kg * fruta_precio
#NaN
1 + np.NaN
#Ejemplo
df_precio_fruta = DataFrame({
    'tienda_1' : [1.95, 1.90, 1.50, 2.60],
    'tienda_2' : [1.80, 1.95, 1.60, 2.40]
}, index = ["manzana", "naranja", "peras", "uvas"])
#compra en cada tienda
lista_compra_1 = Series({"peras" : 1.5, "naranja" : 3})
lista_compra_2 = Series({"manzanas" : 1})
df_lista_compra = DataFrame({
    'tienda_1' : lista_compra_1,
    'tienda_2' : lista_compra_2
})
#operamos
df_precio_fruta * df_lista_compra
#broadcasting
lista_compra = Series ({"peras" : 1.5, "naranjas" : 3, "manzanas" : 1})
#multiplicamos la lista por los precios de cada tienda
df_precio_fruta.multiply(lista_compra, axis = 0)
#Trabajando con valores ausentes o nulos
fruta_kg = Series({'peras' : 2, 'manzanas' : 1, 'naranjas' : 3})
fruta_precio = Series({'manzanas' : 1.95, 'naranja' : 1.90, 'peras' : 1.50, 'uva' : 2.60})
fruta_res =fruta_kg * fruta_precio
fruta_res.isnull()
fruta_res.notnull()
#quitar los valores nulos
fruta_res.dropna()
df_cuenta = DataFrame({
    "tienda_1" : Series({"peras" : 2.25, "naranjas" : 5.70}),
    "tienda_2" : Series({"peras" : 2.40, "naranjas" : 5.85, "uva" : 3}),
    "tienda_3" : Series({"manzanas" : 1.70, "peras" : 2.30, "naranjas" : 5.70, "uva" : 3})
})
df_cuenta.dropna()
#quitar las columnas con Nas
df_cuenta.dropna(axis=1)
#remplazar NaN por otro valor
fruta_res.fillna(0)
#tambien vale mul
fruta_kg.mul(fruta_precio, fill_value=0)
#Utilizando funciones matemáticas universales
s1 = Series([1, 2, 3, 4])
#raiz cuadrada
np.sqrt(s1)
#logaritmos
df1 = DataFrame({
    "x" : s1,
    "y" : np.tanh(s1)
})
np.log(df1)
#Funciones básicas de agregación y estadísticas
df_pesos = DataFrame({
    "p1" : [ 82.9, 79.5, 80.1, None, 78.9],
    "p2" : [ 63.8, 63. , 63.7, 65.2, 65.2],
    "p3" : [ 73.5, 72.3, 71.8, 71.4, 69. ]
}, index = [2012, 2013, 2014, 2015, 2016])
df_pesos.mean()
#calcular la media
df_pesos.mean(axis='columns')
#tenga en cuenta los NaN
df_pesos.mean(skipna=False)
#Índices jerárquicos
meteo_mes = pd.read_csv("./U09_datasets/meteo_mes_agg.csv", sep = ";")
meteo_mes.head(8)
#ajustar el indice
meteo_mes.set_index(["año", "mes"], inplace=True) #decuelve una copia
meteo_mes.head(10)
meteo_mes.index
#refinir el indice
meteo_mes.reset_index(inplace=True)
meteo_mes.head()
#definimos un nuevo indice
meteo_mes.set_index(["ciudad", "año", "mes"], inplace=True)
meteo_mes.head(10)
#Seleccionar elementos
#Mediante etiquetas
meteo_mes.loc[("Bilbao", 2015, 1), :]
#todas la fila spara bilbao
meteo_mes.loc[("Bilbao", ), :].head()
#reordenar un indice
meteo_mes.sort_index(level=0, axis=0, inplace=True)
meteo_mes.loc[("Bilbao", ), :].head()
#extraer DataFrames parciales
bilbao =  meteo_mes.loc[("Bilbao",), :]
valencia = meteo_mes.loc[("Valencia",) , :]
zgz = meteo_mes.loc[("Zaragoza",), :]
#combinamos los datos en un DataFrame
meteo_bvz = pd.concat([bilbao, valencia, zgz], axis=1)
meteo_bvz.head()
#índice mulyinivel
idx = pd.MultiIndex.from_product([["Bilbao", "Valencia", "Zaragoza"], ["temp_c", "viento_vel_kmh"]], names=["ciudades", "variable"])
#remplazamos el indice con los nombres de columnas actuales por el nuevo índice multinivel
meteo_bvz.columns = idx
meteo_bvz.head()
#indicar solo el primer nivel
meteo_bvz["Valencia"].head()
#indicar todos los niveles
meteo_bvz[("Valencia", "temp_c")].head()
#seleccionar simultáneamente por filas y columnas multinivel
meteo_bvz.loc[(2016, [1,3]), "Bilbao"]
#seleccionar rebanas
ixs = pd.IndexSlice
meteo_bvz.loc[ixs[2016, 2:5], ixs["Bilbao", :]]
#Transformando datos
#concatenarlos
df1 = DataFrame({'x' : np.arange(1,5), 'y' : np.arange(5,9)})
df2 = DataFrame({'x' : np.arange(1,4), 'y' : np.arange(11,14)})
print(df1)
print(df2)
#concatenar las filas
pd.concat([df1, df2])
#descarte indices originales y cree nuevos
pd.concat([df1, df2], ignore_index=True)
#concatenra columnas
pd.concat([df1, df2], axis='columns')
#para evitar datos repetidos, añadir un nivel de etiquetado
pd.concat([df1, df2], axis='columns', keys=["DF1", "DF2"])
#tambien para concatenar (devuelve uno nuevo copiando los datos)
df1._append(df2)
#Combinar datos
peliculas = pd.read_csv("./U09_datasets/sample_movie_list.csv", sep = ";")
peliculas.head()
valoracion = pd.read_csv("./U09_datasets/sample_movie_rating.csv", sep = ";")
valoracion.head()
pd.merge(peliculas, valoracion).head() #cruzar los datos
#renstringir manualmente que columnas usar como clave de unión
pd.merge(peliculas, valoracion, on=['title']).head()
#vamos a ver cuantas filas tengo
print("Filas en peliculas:", peliculas.shape[0])
print("Filas en valoraciones:", valoracion.shape[0])
print("Filas en merge:", pd.merge(peliculas, valoracion).shape[0])
#el merge incluya todas las filas
pd.merge(peliculas, valoracion, how='left').head()
#a veces los nombres de las columnas no aparecen igual
generos = pd.read_csv("./U09_datasets/sample_movie_genres.csv", sep = ";")
generos.head()
#indicar explicitamente que columnas usar como claves
pd.merge(peliculas, generos, left_on="title", right_on="movie_title").head()
#rechazar una columna
pd.merge(peliculas, generos, left_on="title", right_on="movie_title").drop("movie_title", axis="columns").head()
#indice común a nivel de filas
peliculas.set_index("title", inplace=True)
generos.set_index("movie_title", inplace=True)
pd.merge(peliculas, generos, left_index=True, right_index=True).head()
#un metodo mas directo
peliculas.join(generos).head()
#Ordenando elementos
temp_mensual = Series([7.2, 7.3, 12.1, 15.7, 20.3, 24.8, 28.2, 25.6, 20.8, 16.8, 12.3, 7.8],
                      index = ["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"])
temp_mensual.sort_values()
#por columnas
df_meteo = DataFrame({'imes' : np.arange(1, 13),
                 'temp_c' :temp_mensual,
                 'lluvia_mm' : [21, 22, 19, 39, 44, 26, 17, 17, 30, 36, 30, 21],
                 'humedad' : [75, 67, 59, 57, 54, 49, 47, 51, 57, 67, 73, 76]},
                columns = ['mes', 'imes', 'temp_c', 'lluvia_mm', 'humedad'],
                index = ["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"])
df_meteo.sort_values("lluvia_mm")
#ordenar lexicográficamente
df_meteo.sort_index()
#Eliminar duplicados
reparto = pd.read_csv("./U09_datasets/sample_movie_cast.csv", sep = ";")
reparto.head()
#extraemos solo los actores
actores = reparto[["actor_name", "actor_fb_likes"]].copy()
actores.head()
#mirar si algo esta duplicado
actores.duplicated(["actor_name"]).any()
#eliminar las filas duplicadas
actores.drop_duplicates(["actor_name"], inplace=True)
actores.duplicated(["actor_name"]).any()
#Aplicando funcionas
#calcular la diferencia entre ingreso y presupuesto de cada película
peliculas.apply(lambda p: p.gross - p.budget, axis="columns").head()
#discretizando variables
#tomamos el año de estreno de las películas
peliculas['year'].head()
#dividir en intervalos
pd.cut(peliculas['year'], bins=[1900, 1980, 1990, 2000, 2010, np.Inf]).head()
decadas = pd.cut(peliculas['year'], 
                 bins=[1900, 1980, 1990, 2000, 2010, np.Inf],
                 labels=['<1980', '1980s', '1990s', '2000s', '>2010'])
pd.Series(decadas).value_counts()
#Agrupando y agregando datos
meteo_mes = pd.read_csv("./U09_datasets/meteo_mes_agg.csv", sep = ";")
#calculamos ell promedio medio agrupando
meteo_mes.groupby('ciudad').mean()
#indexamos columnas sobre el resultado antes de aplicar la funcion
meteo_mes.groupby('ciudad')['temp_c'].mean()
#valor promedio agrupando por ciudad y año
meteo_mes.groupby(['ciudad', 'año'])['temp_c'].mean().head()
#al agrupar varias columnas, tenemos un índice jerárquico
meteo_mes.groupby(['ciudad', 'año'])['temp_c'].mean().index
#devuelve un objeto, una coleccion de DataFrames
meteo_mes.groupby('ciudad')
#Agregados sobre grupos
#agrupamos por ciudad y calculamos media y mediana de temp y velocidad de viento para cada ciudad
meteo_mes.groupby('ciudad')[['temp_c', 'viento_vel_kmh']].aggregate(['mean', np.median, lambda x: min(x)])
#Filtrado de grupos
#descartar ciudades cuya velocidad de viento promedio supere los 12km/h
meteo_mes.groupby('ciudad').filter(lambda x: x['viento_vel_kmh'].mean() < 12).head()
#transformacion de datos por grupos
#normalizamos la variable temperatura por grupos
Z_temp_c = meteo_mes.groupby('ciudad')['temp_c'].transform(lambda x: (x - x.mean())/x.std())
pd.concat([meteo_mes, Z_temp_c], axis='columns').head()
#Aplicando funciones arbitrarias
#función que añade una nueva columna (con la variable temperatira normalizada)
def fnorm(x):
    x['Z_temp_c'] = (x['temp_c'] - x['temp_c'].mean())/x['temp_c'].std()
    return x
#aplicar la función por grupos
meteo_mes.groupby('ciudad').apply(fnorm).head()
#Reorganizando filas y columnas (Tablas resumen)
meteo_mes.groupby(["ciudad", "año"])['temp_c'].mean().head()
#valores promedio organizados en columnas
meteo_mes.groupby(['ciudad', 'año'])['temp_c'].mean().unstack()
#lo mismo en filas
meteo_col_aggs = meteo_mes.groupby('ciudad')[['temp_c', 'viento_vel_kmh']].agg({'temp_c': ['mean', np.median, lambda x: min(x)], 'viento_vel_kmh': ['mean', np.median, lambda x: min(x)]})
meteo_col_aggs
#apilar como filas el primer nivel del eje de columnas
meteo_col_aggs.stack(level = 0).head()
#crear tabla resumen (temperatura promedio, de cada ciudad (filas) u año (columnas))
meteo_mes.pivot_table('temp_c', index= 'ciudad', columns= 'año', aggfunc= 'mean')