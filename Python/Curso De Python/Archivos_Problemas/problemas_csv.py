#Cambiar el tipo de dato de una columna
import pandas as pd
df = pd.read_csv("Archivos_Problemas\\datos.csv")

#convertir a string los datos de una columna
df['edad'] = df['edad'].astype(str)

#mostrar el tipo de dato del primer elemento de la columna edad
#print(type(df['edad'][0]))

#remplazando los datos "Gimenes" por "UnCapo"
df['apellido'].replace("Gimenes","UnCapo",inplace=True)

#mostrando la columna apellido
#print(df['apellido'])

#eliminando las filas con datos faltantes
df = df.dropna()

#eliminando las filas repetidas
df = df.drop_duplicates()

#creando un CSV con el dataframe resultante (limpio)
df.to_csv("Archivos_Problemas\\datos_limpios.csv")
