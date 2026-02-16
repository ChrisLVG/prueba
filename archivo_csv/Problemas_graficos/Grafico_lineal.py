import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("archivo_csv\\Problemas_graficos\\Fumador.csv", names=["fecha","cigarrillos"])

#creando un grafico lineal con seaborn
sns.lineplot(data=df, x="fecha", y="cigarrillos")

#estableciendo un punto especifico en el grafico
plt.plot("01-08", 10, marker="o") #marker para marcar los puntos, linestyle para definir el estilo de la linea, color para definir el color de la linea

plt.show()