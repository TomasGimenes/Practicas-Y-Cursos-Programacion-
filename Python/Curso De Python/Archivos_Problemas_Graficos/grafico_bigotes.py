import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Archivos_Problemas_Graficos\\bigotes.csv")

#creando el grafico
sns.boxplot(x="categoria",y="valor",data=df)

#muestra el grafico
plt.show()