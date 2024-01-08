import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Archivos_Problemas_Graficos\\pedos.csv")

#creando el grafico
sns.lineplot(x="fecha",y="pedos",data=df)

#creando un punto en el punto mas alto
plt.plot("01-09",17,"o")

#meustra el grafico
plt.show()