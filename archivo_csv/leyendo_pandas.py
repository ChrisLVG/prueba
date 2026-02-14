#importamos la libreria pandas
from numpy import integer
import pandas as pd
#usamos la funcion read_csv para leer el archivo csv y lo guardamos en un dataframe y definimos los nombres de las columnas
df=pd.read_csv("archivo_csv\\datos.csv", names=["nombre","edad","Universidad"])
df_removiendo_fila=pd.read_csv("archivo_csv\\datos.csv", names=["nombre","edad","Universidad"], skiprows=1) #remueve la primera fila del archivo csv
df2=df=pd.read_csv("archivo_csv\\datos.csv", names=["nombre","edad","Universidad"])

# obtenemos la informacion de la columna nombre
nombres=df["nombre"]

#ordenar dataframe por edad de menor a mayor
df_ordenado_ascendente=df.sort_values("edad")

#ordenar dataframe por edad de mayor a menor
df_ordenado_descendente=df.sort_values("edad", ascending=False)

#concatenando dos dataframes
df_concatenado=pd.concat([df, df2], ignore_index=True) #ignore_index=True para resetear el indice del nuevo dataframe concatenado

#obteniendo las primeras filas del dataframe en un rango de indices
primeras_filas=df.head(2) 

#obteniendo las ultimas filas del dataframe en un rango de indices
ultimas_filas=df.tail(2) 

#obteniendo un rango de filas del dataframe
rango_filas=df[1:4] #obtiene las filas desde el indice 1 hasta el indice 4 (sin incluir el indice 4)

#obteniendo numero de filas y columnas del dataframe
cantidad=df.shape #devuelve una tupla con el numero de filas y columnas del dataframe en ese orden (filas, columnas)
filas_totales=df.shape[0] #devuelve el numero de filas del dataframe
columnas_totales=df.shape[1] #devuelve el numero de columnas del dataframe

#obteniendo informacion estadistica del dataframe
estadistica=df.describe() #devuelve un resumen estadistico de las columnas numericas del dataframe, incluyendo la cantidad de valores, media, desviacion estandar, valor minimo, percentiles y valor maximo

#obteniendo informacion de una columna especifica del dataframe
informacion_columna=df["edad"].describe() #devuelve un resumen estadistico de la columna "edad", incluyendo la cantidad de valores, media, desviacion estandar, valor minimo, percentiles y valor maximo

#obteniendo informacion de una fila especifica del dataframe
informacion_fila=df.loc[0] #devuelve la informacion de la primera fila del dataframe (indice 0)
informacion_fila_columna=df.loc[2,"nombre"] #devuelve el valor de la columna "nombre" de la tercera fila del dataframe (indice 2)
visualizacion_diferente=df.loc[2,:] #devuelve la informacion de la tercera fila del dataframe (indice 2) en formato de serie, mostrando el nombre de cada columna y su valor correspondiente para esa fila

#obteniendo informacion de todas las filas de una columna
informacion_columna_todas_filas=df["nombre"] #devuelve una serie con los valores de la columna "nombre" para todas las filas del dataframe

#obteniendo informacion condicional
info=df.loc[df["edad"]>20] #devuelve un nuevo dataframe con las filas donde el valor de la columna "edad" es mayor a 20

#modificando el valor de una celda especifica del dataframe
df.replace(to_replace="Emerlinda", value="Helen", inplace=True) #reemplaza el valor "Juan" por "Carlos" en todo el dataframe, inplace=True para modificar el dataframe original

#borrando una fila del dataframe
#df.drop(index=1, inplace=True) #borra la fila con el indice 1

#borrando una fila condicional del dataframe
#df.drop(index=df[df["nombre"]=="Emerlinda"].index, inplace=True) #borra las filas donde el valor de la columna "nombre" es igual a "Emerlinda"

#borrando una fila con valores nulos del dataframe
df.dropna(inplace=True) #borra las filas que contienen valores nulos en cualquier columna del dataframe

#borrando filas repetidas del dataframe
df.drop_duplicates(inplace=True) #borra las filas que son exactamente iguales en todas las columnas

#borrando una columna del dataframe
#df.drop(columns=["Universidad"], inplace=True)

#Guardando el dataframe modificado en un nuevo archivo csv
df.to_csv("archivo_csv\\datos_modificados.csv", index=False) #index=False para no guardar el indice del dataframe en el archivo csv