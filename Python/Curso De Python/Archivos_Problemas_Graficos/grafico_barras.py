import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Archivos_Problemas_Graficos\\cofla_ingresos.csv")

#creando el grafico
sns.barplot(x="fuente",y="ingresos",data=df)

#obtenendo el total de ingresos
total_ingresos = df['ingresos'].sum()

#mostrando el total
print(f"El total de ingresos es de: ${total_ingresos} USD")

#meustra el grafico
plt.show()