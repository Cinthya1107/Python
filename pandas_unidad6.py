#PANDAS
#Series
import numpy as np
import pandas as pd 
from pandas import Series, DataFrame
s1 = Series([3,5,7,9])
print(s1)
#Ejemplo con índices
temp_anual = Series([16.6, 16.2, 15.5, 17.0, 16.6, 16.5], index=[2011, 2012, 2013, 2014, 2015, 2016])
print(temp_anual)
#Etiquetas con texto
temp_mensual = Series([7.2, 7.3, 12.1, 15.7, 20.3, 24.8, 28.2, 25.6, 20.8, 16.8, 12.3, 7.8], index=["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"])
print(temp_mensual)
#Seleccionar un elemento por su posición
s1 = Series([3,5,7,9])
print(s1[2])
#Seleccionar una "rebanada"
print(s1[1:3])
#Máscara Booleana
print(s1[s1<6])
#Seleccionar un valor por índice
print(temp_mensual["Ene"])
#Seleccionar usando una lista de etiquetas o índices
print(temp_mensual[["Mar", "Abr", "May"]])
#Producto escalar
print(s1 * 2)
#Operaciones elemento a elemento entre series
s2 = Series([2,3,4,5])
print(s1 - s2)
print(s1.sum())
print(s1.prod())

#DataFrames
#Se crea como un diccionario
df1 = DataFrame({'mes' : ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"], 
                 'temp_c' : [7.2, 7.3, 12.1, 15.7, 20.3, 24.8, 28.2, 25.6, 20.8, 16.8, 12.3, 7.8],
                 'lluvia_mm' : [21, 22, 19, 39, 44, 26, 17, 17, 30, 36, 30, 21],
                 'humedad' : [75, 67, 59,57, 54, 49, 47, 51, 57, 67, 73, 76]},
                columns=['mes', 'temp_c', 'lluvia_mm', 'humedad'])
print(df1)

df2 = DataFrame({'mes' : ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"], 
                 'imes' : np.arange(1,13),
                 'temp_c' : [7.2, 7.3, 12.1, 15.7, 20.3, 24.8, 28.2, 25.6, 20.8, 16.8, 12.3, 7.8],
                 'lluvia_mm' : [21, 22, 19, 39, 44, 26, 17, 17, 30, 36, 30, 21],
                 'humedad' : [75, 67, 59,57, 54, 49, 47, 51, 57, 67, 73, 76]},
                columns=['mes', 'imes', 'temp_c', 'lluvia_mm', 'humedad'])
print(df2)

#Definir indices
df3 = DataFrame({'imes' : np.arange(1,13),
                 'temp_c' : temp_mensual,
                 'lluvia_mm' : [21, 22, 19, 39, 44, 26, 17, 17, 30, 36, 30, 21],
                 'humedad' : [75, 67, 59,57, 54, 49, 47, 51, 57, 67, 73, 76]},
                columns=['imes', 'temp_c', 'lluvia_mm', 'humedad'],
                index= ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"])
print(df3)

#Índice asociado al DataFrame
print(df3.index)
#Columnas del DataFrame 
print(df3.columns)
#Tamaño del DatafRame 
print(df3.shape)
#Número de filas
print(df3.shape[0])
#Tamaño total (número de elementos)
print(df3.size)
#Mostrar las N primeras filas (5 por defecto)
print(df3.head())
#O las N últimas
print(df3.tail(3))
#Contar elementos no nulos en cada columna
print(df3.count())
#Resumen con estadísticas básicas de cada columna
print(df3.describe())

#MÁS SPBRE SELECCIÓN Y FILTRADO
df_meteo = DataFrame({'imes' : np.arange(1,13),
                     'temp_c' : [7.2, 7.3, 12.1, 15.7, 20.3, 24.8, 28.2, 25.6, 20.8, 16.8, 12.3, 7.8],
                     'lluvia_mm' : [21, 22, 19, 39, 44, 26, 17, 17, 30, 36, 30, 21],
                     'humedad' : [75, 67, 59,57, 54, 49, 47, 51, 57, 67, 73, 76]},
                     columns=['imes', 'temp_c', 'lluvia_mm', 'humedad'],
                     index=["Ene","Feb","Mar","Abr","May","Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"])
#Acceder a una columna
print(df_meteo["lluvia_mm"])
#Acceder a una columna como si fuera un atributo
print(df_meteo.temp_c)

df_geom = DataFrame({'shape': ["triangle", "square", "circle"], 
                     'area' : ["b*h/2", "a*a", "PI*r*r"]})
#Accedemos a la columna "shape"
df_geom["shape"]
print(df_geom.shape)
#Accedemos a un atributo propio de la clase, nos dice el número de filas y columnas tiene
print(df_geom.shape)
print(df_meteo[["imes", "temp_c"]])
#Indicamos un rango/"rebanada" de índice
print(df_meteo[0:4])
#Rebanadas de etiquetas
print(df_meteo["Ene" : "Mar"]) #De Enero a Marzo
#Seleccionar las filas en la que temperatura supere los 20 grados
print(df_meteo[df_meteo.temp_c > 20.0])
#Seleccionar un elemento concreto
print(df_meteo.loc["May", "lluvia_mm"])
#Seleccionar una fila entera
print(df_meteo.loc["May", ])
#Seleccionar una columna entera
print(df_meteo.loc[:, "humedad"])
#Seleccionar sunconjunto de filas y columnas
print(df_meteo.loc["Feb":"Abr", ["lluvia_mm", "humedad"]])

#Acceso mediante índices de posición
print(df_meteo.iloc[6,2])
#Seleccionar una fila entera
print(df_meteo.iloc[6, ])
#Seleccionar una columna entera
print(df_meteo.iloc[:, 1])
#Seleccionar subconjuto de filas y columnas
print(df_meteo.iloc[0:3, 1:3])

#Aumentar un grado la temperatura de los meses de Junio a Agosto
df_meteo.loc["Jun":"Ago", "temp_c"] = df_meteo.loc["Jun":"Ago", "temp_c"] + 1
print(df_meteo)
#Añadir una columna, con un mismo valor para todas las filas
df_meteo["limite_temp_c"] = 50
print(df_meteo)
#Añadir una columna, dando valores individuales a cada elemento
#Pasar la temperatura de grados centigrados a fahrenheit
df_meteo["temp_F"] = 1.8 * df_meteo["temp_c"] + 32
print(df_meteo)

#LEYENDO DATOS DE FICHERO
#Ruta de direcctorios
df_flights = pd.read_csv("C:/Users/EQUIPO/Desktop/Limpio/INFORMATICA/MASTERD/U09_datasets/NYC_flights_2013_MINI.csv", sep=";")
#Vemos el tamaño
print(df_flights.shape)
#Mostramos las primeras filas y columnas del DataFrame
print(df_flights.iloc[0:5, 0:10])

#ESCRIBIENDO LOS DATOS A FICHERO
#Seleccionamos las primeras filas 
df_mini = df_flights.head()
#Guardamos en fichero
df_mini.to_csv("./Prueba_export_pandas.csv", sep= ";", na_rep= "", header= True, index= False, index_label= False)

#OPERACIONES BINARIAS/ ALINEACIÓN DE ÍNDICES
#Definimos dos series
fruta_kg = Series({'peras' : 2, 'manzanas' : 1, 'naranjas' : 3})
fruta_precio = Series({'manzanas' : 1.9, 'naranjas' : 1.90, 'peras' : 1.50, 'uva' : 2.50})
fruta_res = fruta_kg * fruta_precio
print(fruta_res )
#Preparamos un DataFrame con precios de dos tiendas
df_precio_fruta = DataFrame({'tienda_1' : [1.95, 1.90, 1.50, 2.60],
                             'tienda_2' : [1.80, 1.95, 1.69, 2.40]},
                            index= ["manzanas", "naranjas", "peras", "uvas"])
#Y otro DatFrame con la compra en cada unan de las tiendas
lista_compra_1 = Series({"peras" : 1.5, "naranjas" : 3})
lista_compra_2 = Series({"manzanas" : 1})
df_lista_compra = DataFrame({'tienda_1' : lista_compra_1, 'tienda_2' : lista_compra_2})
#Operamos con ambos DataFrames
df_precio_fruta * df_lista_compra

lista_compra = Series({"peras" : 1.5, "naranjas" : 3, "manzanas" : 1})
#Multiplicamos la lista de la compra por los precios de cada tienda
df_precio_fruta.multiply(lista_compra, axis=0)

#TRABAJANDO CON VALORES AUSENTES O NULOS
#Vemos que elementos son nulos
print(fruta_res.isnull())
#Vemos que elementos no son nulos
print(fruta_res.notnull())
print(fruta_res.dropna())
#Descartar filas con NAs
df_cuenta = DataFrame({"tienda_1" : Series({"peras" : 2.25, "naranjas" : 5.70}),
                       "tienda_2" : Series({"peras" : 2.40, "naranjas" : 5.85, "uvas" : 2.60}),
                       "tienda_3" : Series({"manzanas" : 1.70, "peras" : 2.30, "naranjas" : 5.70, "uvas" : 3})})
print(df_cuenta.dropna())
#O las columnas con NAs
print(df_cuenta.dropna(axis=1))
#Remplazar NaN por otro valor
print(fruta_res.fillna(0))
#Si usamos el método aritmético 'mul', en vez de *, podemos usar el argumento 'fill value'
print(fruta_kg.mul(fruta_precio, fill_value=0))

#UTILIZANDO FUNCIONES MATEMÁTICAS UNIVERSALES
s1 = Series([1,2,3,4])
#Raíz cuadrada
print(np.sqrt(s1))
#Sobre un DataFrame
df1 = DataFrame({"x" : s1, "y" : np.tanh(s1)})
#Logaritmos
print(np.log(df1))

#FUNCIONES BÁSICAS DE AGREGACIÓN Y ESTADÍSTICAS
df_pesos = DataFrame({"p1" : [82.9, 79.5, 80.1, None, 78.9],
                      "p2" : [63.8, 63.0, 63.7, 65.2, 65.2],
                      "p3" : [73.5, 72.3, 71.8, 71.4, 69.0]},
                     index= [2012, 2013, 2014, 2015, 2016])
#Calcular el peso medio
print(df_pesos.mean())
#Calcular el peso medio observados cada año
print(df_pesos.mean(axis= 'columns'))
print(df_pesos.mean(skipna= False))

#ÍNDICES JERÁRQUICOS
meteo_mes = pd.read_csv("C:/Users/EQUIPO/Desktop/Limpio/INFORMATICA/MASTERD/U09_datasets/meteo_mes_agg.csv", sep=";")
print(meteo_mes.head(8))
#Ajustamos el índice del DataFrame (que use las columnas 'año' y 'mes')
meteo_mes.set_index(["año", "mes"], inplace=True)
print(meteo_mes.head(10))
print(meteo_mes.index)
#Redefinir el índice
meteo_mes.reset_index(inplace=True)
print(meteo_mes.head())
#Otro ejemplo
meteo_mes.set_index(["ciudad", "año", "mes"], inplace=True)
print(meteo_mes.head(10))

#SELECCIÓN DE ELEMENTOS
#Seleccionar un elemento mediante etiquetas
print(meteo_mes.loc[("Bilbao", 2015, 1), :])
#Restringimos solo el primer nivel de índice
print(meteo_mes.loc[("Bilbao",), : ].head())
#Reordenar el índice de filas (axis = 0)
meteo_mes.sort_index(level=0, axis=0, inplace=True)
print(meteo_mes.loc[("Bilbao", ), :].head())

#ÍNDICES JERÁRQUICOS SOBRE COLUMNAS
bilbao = meteo_mes.loc[("Bilbao", ), :]
valencia = meteo_mes.loc[("Valencia", ), :]
zgz = meteo_mes.loc[("Zaragoza", ), :]
#Los convinamos en un solo DataFrame
meteo_bvz = pd.concat([bilbao, valencia, zgz], axis=1)
print(meteo_bvz.head())
#Crear un índice multinivel
idx = pd.MultiIndex.from_product([["Bilbao", "Valencia", "Zaragoza"],
                            ["temp_c", "viento_vel_kmh"]],
                           names= ["ciudad", "variable"])
#Remplazamos el índice con los nombres de columnas actuales
meteo_bvz.columns = idx
#Indicando solo el primer nivel
print(meteo_bvz["Valencia"].head())
#Especificando los niveles
print(meteo_bvz[("Valencia", "temp_c")].head())
#Seleccionar simultáneamente por filas y columnas multinivel
print(meteo_bvz.loc[(2016, [1,3]), "Bilbao"])
#Creamos un obejro IndexSlice y lo usamos para seleccionar rebanadas
ixs = pd.IndexSlice
print(meteo_bvz.loc[ixs[2016, 2:5], ixs["Bilbao", :]])

#TRANSFORMANDO LOS DATOS
#CONCATENANDO DATOS
df1 = DataFrame({'x' : np.arange(1,5), 'y' : np.arange(5,9)})
df2 = DataFrame({'x' : np.arange(1,4), 'z' : np.arange(11,14)})
print(df1)
print(df2)
#Concatenamos las filas de dos DataFrame
print(pd.concat([df1, df2]))
#Descarte los índices originales y cree nuevos
print(pd.concat([df1, df2], ignore_index=True))
#Concatenar columnas
print(pd.concat([df1, df2], axis = 'columns'))
#Para lidiar con los nombres de filas/columnas repetidas, añadimos un nivel por DataFrame que combinamos
print(pd.concat([df1, df2], axis='columns', keys=["DF1","DF2"]))
#Un atajo
#print(df1.append(df2)) Esta deprecated

#Combinando Datos: Merge y Join
peliculas = pd.read_csv("C:/Users/EQUIPO/Desktop/Limpio/INFORMATICA/MASTERD/U09_datasets/sample_movie_list.csv", sep=";")
valoraciones = pd.read_csv("C:/Users/EQUIPO/Desktop/Limpio/INFORMATICA/MASTERD/U09_datasets/sample_movie_rating.csv", sep=";")
generos = pd.read_csv("C:/Users/EQUIPO/Desktop/Limpio/INFORMATICA/MASTERD/U09_datasets/sample_movie_genres.csv", sep=";")
print(peliculas.head())
print(valoraciones.head())
print(generos.head())
#Cruzar los dos DataFrames
#Merge: Usa las columnas con el mismo nombre para usarlas como clave de unión
print(pd.merge(peliculas, valoraciones).head())
#Indicar o restringir manualmnete las claves de unión
print(pd.merge(peliculas, valoraciones, on=['title']).head())
#Cuantas filas tenemos en cada DataFrame
print("Filas en películas:", peliculas.shape[0])
print("Filas en valoraciones", valoraciones.shape[0])
print("Filas en merge", pd.merge(peliculas, valoraciones).shape[0])
#Con merge se ignoran las películas sin valoración, pero se pueden tener en cuenta con 'left', 'right' o 'outer'
print(pd.merge(peliculas, valoraciones, how='left').head())
pd.merge(peliculas, valoraciones, how='right').head()
pd.merge(peliculas, valoraciones, how='outer').head()
#Cuando hay más de dos DataFrames se usan 'left_on' o 'right_on'
print(pd.merge(peliculas, generos, left_on="title", right_on="movie_title").head())
#Descartar una columna
print(pd.merge(peliculas, generos, left_on="title", right_on="movie_title").drop("movie_title", axis="columns").head())
#Hacer un cruce , usando un índice común a nivel de filas
peliculas.set_index("title", inplace=True)
generos.set_index("movie_title", inplace=True)
print(pd.merge(peliculas, generos, left_index=True, right_index=True).head())
#Otra opción
print(peliculas.join(generos).head())

#Ordenación Elementos
#Ordenar por valores
print(temp_mensual.sort_values())
#Ordenar por una columna en concreto
print(df_meteo.sort_values("lluvia_mm"))
#Ordenar por el índice
print(df_meteo.sort_index())

#Eliminar Duplicados
reparto = pd.read_csv("C:/Users/EQUIPO/Desktop/Limpio/INFORMATICA/MASTERD/U09_datasets/sample_movie_cast.csv", sep=";")
print(reparto.head())
#Extraer solo a los actores
actores = reparto[["actor_name","actor_fb_likes"]].copy()
print(actores.head())
#Averiguar si hay actores duplicados
print(actores.duplicated(["actor_name"]).any())
#Eliminar las duplicadas
actores.drop_duplicates(["actor_name"], inplace=True)
print(actores.duplicated(["actor_name"]).any())

#Aplicando Funciones
#Calcular la diferencia entre ingresos y presupuesto de cada película
print(peliculas.apply(lambda p: p.gross - p.budget, axis="columns").head())

#Discretizando variables
#Tomamos el año de estreno de las películas
print(peliculas['year'].head())
#Dividimos en intervalos
print(pd.cut(peliculas['year'], bins=[1900, 1980, 1990, 2000, 2010, np.inf]).head())
#Contar cuántos casos hay en cada rango
decadas = pd.cut(peliculas['year'],
                 bins=[1900, 1980, 1990, 2000, 2010, np.inf],
                 labels=['<1980', '1980s', '1990s', '2000s', '>2010'])
print(pd.value_counts(decadas))

#AGRUPANDO Y AGREGANDO DATOS
meteo_mes = pd.read_csv("C:/Users/EQUIPO/Desktop/Limpio/INFORMATICA/MASTERD/U09_datasets/meteo_mes_agg.csv", sep=";")
#Calculamos valores promedio agrupando por ciudad
print(meteo_mes.groupby('ciudad').mean())
#Indexamos las columnas
print(meteo_mes.groupby('ciudad')['temp_c'].mean())
#Agrupar más de una columna
print(meteo_mes.groupby(['ciudad', 'año'])['temp_c'].mean().head())
#Tenemos un índice jerárquico para las filas
print(meteo_mes.groupby(['ciudad', 'año'])['temp_c'].mean().index)

#Agregados sobre grupos
#Calcular múltiples valores agregados de forma simultánea
print(meteo_mes.groupby('ciudad')[['temp_c', 'viento_vel_kmh']].aggregate(['mean', np.median, lambda x: min(x)]))

#Filtrado de grupos
print(meteo_mes.groupby('ciudad').filter(lambda x: x['viento_vel_kmh'].mean() < 12).head())

#Transformación de datos por grupos
#Normalizamos la variable 'temperatura' por grupos
Z_temp_c = meteo_mes.groupby('ciudad')['temp_c'].transform(lambda x: (x - x.mean())/x.std())
print(pd.concat([meteo_mes, Z_temp_c], axis='columns').head())

#Aplicando funciones arbitrarias
#Función que añade una nueva columna
def fnorm(x):
    x['Z_temp_c'] = (x['temp_c'].mean())/x['temp_c'].std()
    return x
print(meteo_mes.groupby('ciudad').apply(fnorm).head())

#Reorganizando filas y columnas. Tablas resumen
#Valor promedio agrupando por ciudad y año
print(meteo_mes.groupby(['ciudad', 'año'])['temp_c'].mean().head())
#Organizados en columnas
print(meteo_mes.groupby(['ciudad','año'])['temp_c'].mean().unstack())
#En filas
meteo_col_aggs = meteo_mes.groupby('ciudad')[['temp_c', 'viento_vel_kmh']].aggregate(['mean', np.median, lambda x: min(x)])
print(meteo_col_aggs)
#Apilar como filas el primer nivel del eje de columnas
print(meteo_col_aggs.stack(level= 0).head())
#Crear una tabla resumen con la temperatura promedio
print(meteo_mes.pivot_table('temp_c', index= 'ciudad', columns='año', aggfunc='mean'))
