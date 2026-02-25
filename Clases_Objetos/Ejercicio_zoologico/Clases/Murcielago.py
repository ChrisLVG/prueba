from Clases import Ave as a, Mamifero as m
class Murcielago(m.Mamifero,a.Ave):
    def __init__(self, nombre, edad, especie, tipo):
        m.Mamifero.__init__(self, nombre, edad, especie)
        a.Ave.__init__(self, nombre, edad, especie)
        self.tipo = tipo

    def comer(self):
        return f"{self.nombre} esta comiendo."