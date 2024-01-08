import pandas as pd

#usando la funcion read_csv para leer el archivo CSV
df = pd.read_csv("Archivos\\datos.csv")
df2 = pd.read_csv("Archivos\\datos.csv")

#obteniando los datos de la columna nombre
nombres = df["nombre"]

#ordenando el datraframe por la edad
df_ordenado_ascendente = df.sort_values("edad")
print(df_ordenado_ascendente)

#ordenando de forma descendente
df_ordenado_descendente = df.sort_values("edad",ascending=False)
print(df_ordenado_descendente)

#concatenando los 2 dataframe
df_concatenado = pd.concat([df,df2])

#accediendo a las primeras 3 filas con head()
primer_fila = df.head(3)

#accediendo a las ultimas 3 filas con tail()
primer_fila = df.tail(3)

#accediendo a la cantidad de filas y columnas con shape
filas_totales,columas_totales = df.shape

#obteniando data estadistica del dataframe
df_info = df.describe()

#accediendo a la edad de la fila 2 con loc
elemento_especifico_loc = df.loc[2,"edad"]

#accediendo a la edad de la fila 2 con iloc
elemento_especifico_iloc = df.iloc[2,2]

#accediendo a todos los apellidos con iloc
apellidos_iloc = df.iloc[:,1]


#accediendo a todos los apellidos con loc
apellidos_loc = df.loc[:,"apellido"]

#accediendo a las filac con edad mayor que 20
mayor_que_20 = df.loc[df["edad"]>20,:]


#TECNICA de slicing
cadena = "0123456789"
#print(cadena[1:4])