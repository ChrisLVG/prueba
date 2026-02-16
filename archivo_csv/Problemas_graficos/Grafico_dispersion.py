import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("archivo_csv\\Problemas_graficos\\Fu.csv", names=["Horas","Ingresos"])

#creando un grafico de dispersion con seaborn
sns.scatterplot(data=df, x="Horas", y="Ingresos")

plt.show()