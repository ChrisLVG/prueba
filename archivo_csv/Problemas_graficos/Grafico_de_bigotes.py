import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("archivo_csv\\Problemas_graficos\\categorias_valores.csv", names=["categoria","valor"])

#creando un grafico de barras con seaborn
sns.boxplot(data=df, x="categoria", y="valor")

plt.show()


