import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("archivo_csv\\Problemas_graficos\\ingresos.csv", names=["trabajo","ingresos"])

#creando un grafico de barras con seaborn
sns.barplot(data=df, x="trabajo", y="ingresos")

plt.show()

#obteniendo el valor total de ingresos
total_ingresos=df["ingresos"].sum() #devuelve la suma de los valores de la columna "ingresos"

print("Total de ingresos: $", total_ingresos)