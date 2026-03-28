class Sentimiento:
    def __init__(self, texto,color):
        self.texto = texto
        self.color = color

    def __str__(self):
        # Pinta solo el texto del sentimiento y vuelve al color normal inmediatamente reemplazando los: {}, por los parametros color y texto en ese orden, el \x1b[0m es para volver al color normal despues de pintar el texto del sentimiento
        return "\x1b[1;{}m{}\x1b[0m".format(self.color, self.texto)