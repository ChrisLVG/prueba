from textblob import TextBlob
import Clases.Sentimiento as s
rangos = {
    "negativo": (-0.6, -0.3, "31"),
    "algo negativo": (-0.3, -0.1, "31"),
    "neutral": (-0.1, 0.1, "33"),
    "algo positivo": (0.1, 0.4, "32"),
    "positivo": (0.4, 0.9, "32"),
    "muy positivo": (0.9, 1.0, "32")
}
class AnalizadorSentimientos:
 def analizar_sentimiento(self, rango):
    for clave, valor in rangos.items():
        if valor[0] <= rango < valor[1]:
            return s.Sentimiento(clave, valor[2])
    return s.Sentimiento("Desconocido", "37")
 
while True:
    texto = input("Ingrese un texto para analizar su sentimiento (o 'salir' para terminar): ")
    if texto.lower() == "salir":
        break
    analizador = AnalizadorSentimientos()
    sentimiento = TextBlob(texto).sentiment.polarity
    resultado = analizador.analizar_sentimiento(sentimiento)
    print(resultado)