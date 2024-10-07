import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import statsmodels.formula.api as smf
#Cargamos los datos meteorologicos
meteo_mes = pd.read_csv("C:/Users/EQUIPO/Desktop/Limpio/INFORMATICA/MASTERD/U09_datasets/meteo_mes_agg.csv", sep=";")
#Crea un gráfico de dispersión (evitando que se solapen los puntos)
sns.swarmplot(x='mes', y='temp_c', data=meteo_mes)
#Distribución de datos
sns.displot(meteo_mes['viento_vel_kmh'])
#Omitir el estimador de densidad y añadir marcadores
sns.displot(meteo_mes['viento_vel_kmh'], kde = False, rug=True)
#Diagrama de caja (boxplot)
sns.boxplot(y='viento_vel_kmh', data=meteo_mes)
#Visualizando relaciones entre variables (Diagrama de dispersión)
movies = pd.read_csv("C:/Users/EQUIPO/Desktop/Limpio/INFORMATICA/MASTERD/U10_datasets/imdb_movie.csv")
sns.jointplot(x = 'movie_facebook_likes', y = 'gross', data= movies)
#Visualizar las películas que tienen datos de likes
movies_fb = movies.loc[movies['movie_facebook_likes'] > 0, ['movie_facebook_likes', 'gross']]
sns.jointplot(x = 'movie_facebook_likes', y ='gross', data= np.log10(movies_fb))
#Mostar densidades de probabilidad estimada
sns.jointplot(x ='movie_facebook_likes', y ='gross', data= np.log10(movies_fb), kind="kde")
#Más modelos
sns.regplot(x ='movie_facebook_likes', y = 'gross', data= np.log10(movies_fb))

#Comparando niveles o categorías
#Añadir colores
sns.swarmplot(x='mes', y='temp_c', data=meteo_mes, hue='ciudad')
#Lo mismo con boxplot
sns.boxenplot(x= 'mes', y= 'temp_c', data= meteo_mes)
#Dividir por otra variable
sns.boxenplot(x='mes', y='temp_c', hue='año', data=meteo_mes)
#Gráfico de violín
sns.violinplot(x='mes', y='temp_c', hue='año', data=meteo_mes)
#Otra forma del gráfico violín
sns.violinplot(x='mes', y='temp_c', hue='año', split=True, data=meteo_mes)
#Gráfico de barras
sns.barplot(x='mes', y='temp_c', hue='año', data=meteo_mes)

#Facets
#Gráficos múltiples organizados en cuadrículas o rejillas
meteo_bvz = meteo_mes[meteo_mes['ciudad'].isin(['Bilbao', 'Valencia', 'Zaragoza'])]
sns.FacetGrid(meteo_bvz, row='año', col='ciudad').map(sns.pointplot, "mes", "temp_c")
#Pintar la rejilla de celdas sin datos
sns.FacetGrid(meteo_bvz, row='año', col='ciudad')
#Usando colores
meteo_bvz_long = pd.melt(meteo_bvz,
                         id_vars=['año', 'mes', 'ciudad'],
                         value_vars=['temp_c', 'viento_vel_kmh'],
                         var_name='variable', value_name='valor')
sns.FacetGrid(meteo_bvz_long, row='variable', col='ciudad', hue='año').map(sns.pointplot, 'mes', 'valor')

#Estilos y Temas 
#darkgrid, whitegrid, dark, white, ticks
sns.set_style('darkgrid', rc={'axes.grid': False})
sns.swarmplot(x='mes', y='temp_c', data=meteo_mes)
#Tamaño de la figura
sns.barplot(x='mes', y='temp_c', hue='año', data=meteo_mes).figure.set_size_inches(10,6)
#Colores

#Variables categóricas
with sns.color_palette("husl", 2):
    sns.barplot(x='mes', y='temp_c', hue='año', data=meteo_mes)
#Decidir los colores manualmente
with sns.xkcd_palette(["red", "blue"]):
    sns.barplot(x='mes', y='temp_c', hue='año', data=meteo_mes)
    
#Variables continuas
#Varien el calor gradual
with sns.light_palette("muted purple", input="xkcd"):
    sns.jointplot(x = 'movie_facebook_likes', y = 'gross', data= np.log10(movies_fb), kind="kde")
#Incremenetar el contraste
cmap = sns.cubehelix_palette(light=1, as_cmap=True)
sns.jointplot(x = 'movie_facebook_likes', y = 'gross', data= np.log10(movies_fb), kind="kde", cmap=cmap)

#Títulos
sns.swarmplot(x='mes', y='temp_c', data=meteo_mes).set_title("Temperaturas mensuales observadas", fontsize = 14)
#Ejes
sns.swarmplot(x='mes', y='temp_c', data=meteo_mes).set(xlabel="Mes", ylabel="Temperatura (ºC)")

#MODELOS LINEALES
#Modelo lineal simple: la variable respuesta depende linealmente de una variable explicativa
#Y= b0 + b1X+ e
ads = pd.read_csv("C:/Users/EQUIPO/Desktop/Limpio/INFORMATICA/MASTERD/U10_datasets/advertising.csv", sep=";")
#Preparamos los datos
ads_m = ads.melt(id_vars='Sales', value_vars=['TV', 'Radio', 'Newspaper'], var_name='Media', value_name='Spend')
#Representamos en una rejilla las ventas según gasto en cada año
sns.FacetGrid(ads_m, col='Media', sharex=False).map(sns.regplot, 'Spend', 'Sales', fit_reg = False)

#Definimos un modelo y ~ b0 + b1*X + e
#Vector respuesta
y = ads['Sales']
#Matriz de variables explicativas del modelo
X = ads['TV']
#Añadimos un término constante a la matriz del modelo (b0)
X = sm.add_constant(X, prepend=False)
#Construimos el objeto modelo (OLS)
model = sm.OLS(y, X)
#Adjustamos los parámetros del modelo (b0, b1)
mfitted = model.fit()
#Veamos el resumen del modelo ajustado
print(mfitted.summary())
#Representado con un gráfico con los valores estimados
fig = plt.figure()
fig = sm.graphics.plot_fit(mfitted, "TV").set_size_inches(10, 6)
#Estimaciones para nuevos datos de entrada
#Generamos unos cuantos valores aleatorios para el gasto de TV
nuevas_obs = np.random.uniform(low=0, high=200, size=10)
#Añadimos la constante
nuevas_obs = sm.add_constant(nuevas_obs, prepend=False)
#Predecir la respuesta
y_pred = mfitted.predict(nuevas_obs)
#Lo pintamos
sns.regplot(x=nuevas_obs[:,0], y=y_pred, fit_reg=False)

#Regresión lineal múltiple
#Sales = b0 + b1TV + b2Radio + b3Newspaper + e
#Vector respuesta
y = ads['Sales']
#Matriz de variables explicativas del modelo
X = ads[['TV', 'Radio', 'Newspaper']]
#Añadimos un término constante a la matriz del modelo (b0)
X = sm.add_constant(X, prepend=False)
#Construimos el objeto modelo (OLS)
model_mlin = sm.OLS(y, X)
#Ajustamos los parámetros del modelo
mlin_fitted = model_mlin.fit()
#Veamos el resumen del modelo ajustado
print(mlin_fitted.summary())
#Ver la relación parcial entre la variable respuesra y cada variable explicativa
fig = plt.figure()
fig = sm.graphics.plot_partregress_grid(mlin_fitted, ['TV', 'Radio', 'Newspaper']).set_size_inches(10, 6)

#Definiendo modelos con fórmulas
#Definimos el modelo usando una formula como en R
model_f = smf.ols(formula= 'Sales ~ TV + Radio + Newspaper', data=ads)
#Ajustamos el modelo
mf_fitted = model_f.fit()
#Resumen
print(mf_fitted.summary())

#Interacciones entre variables
#Si cuando las variables explicativas valen cero, la respuesta es cero, podemos eliminar el intercept
#Sales ~ TV + Radio + Newspaper - 1

#Variables categóricas
#Creamos una variable categórica (¿el gasto en TV en bajo, medio o alto?)
ads['TV_budget'] = pd.qcut(ads['TV'], [0, 0.15, 0.85, 1], labels=['LOW', 'MID', 'HIGH'])
#Creamos una variable entera
#0 si hay más gasto en TV que en el resto
#1 en el caso contrario
ads['More_Radio_Or_News'] = ads.apply(lambda x: int(x['TV'] < x['Radio'] + x['Newspaper']), axis="columns")
#Definimos un modelo usando variables categóricas
model_c = smf.ols(formula= 'Sales ~ TV_budget + C(More_Radio_Or_News)', data=ads)
mc_fitted = model_c.fit()
print(mc_fitted.summary())

#Transformaciones (Funciones en fórmulas)
#Definimos un módelo usando la raíz cuadrada del gasto en TV, como predictor
model_fn = smf.ols(formula= 'Sales ~ np.sqrt(TV)', data=ads)
mfn_fitted = model_fn.fit()
print(mfn_fitted.summary())

#Clasificación (Regresión logística)
body = pd.read_csv("C:/Users/EQUIPO/Desktop/Limpio/INFORMATICA/MASTERD/U10_datasets/body_measures_subset.csv", sep=";")
print(body.head())
import statsmodels.api as sm
# Variable respuesta
y = body['Gender']
# Las variables predictoras son todas las demás
X = body.iloc[:, 1:]
# Añadimos el término constante
X = sm.add_constant(X)
# Construimos el modelo logístico con sm.Logit en lugar de smf.logit
model = sm.Logit(y, X)
# Ajustamos el modelo
mfitted = model.fit()
# Examinamos los resultados del ajuste
print(mfitted.summary())

#La diagonal
print(mfitted.pred_table())

#Creamos el conjunto de entrenamiento tomando aletoriamente el 80% de filas
body_train = body.copy().sample(frac=0.8)
#El conjunto de test es el formando por el resto de filas
body_test = body.copy().drop(body_train.index)
#Variable respuesta
y_train = body_train['Gender']
y_test = body_test['Gender']
#Las variables predictoras son todas las demás
X_train = body_train.iloc[:, 1:]
X_test = body_test.iloc[:, 1:]
#Añadimos el término constante
X_train = sm.add_constant(X_train)
X_test = sm.add_constant(X_test)
#Cosntruimos el modelo logístico
model = sm.Logit(y_train, X_train)
#Y ajustamos
mfitted = model.fit()

#Predicción sobre el conjunto de test
pred = mfitted.predict(X_test)
print(pred.head())

#Tabla de confusión
pred_0_1 = [1 if p >= 0.5 else 0 for p in pred]
pd.crosstab(index=y_test, columns=pd.Categorical(pred_0_1), rownames=['Obs'], colnames=['Pred'])

#Acierto global
acierto_total = np.mean(y_test == pred_0_1)
print('acierto_total = {0}%'.format(np.round(acierto_total*100, 2)))

