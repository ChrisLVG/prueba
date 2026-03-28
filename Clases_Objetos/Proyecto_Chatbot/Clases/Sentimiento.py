class Sentimiento:
    def __init__(self, texto,color):
        self.texto = texto
        self.color = color

    def __str__(self):
        # Pinta solo el texto del sentimiento y vuelve al color normal inmediatamente
        return "\x1b[1;{}m{}\x1b[0m".format(self.color, self.texto)