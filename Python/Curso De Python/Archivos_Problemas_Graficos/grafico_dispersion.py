import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Archivos_Problemas_Graficos\\dispersion.csv")

#creando el grafico
sns.scatterplot(x="tiempo",y="dinero",data=df)

#meustra el grafico
plt.show()