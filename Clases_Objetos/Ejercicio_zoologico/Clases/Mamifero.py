class Mamifero:
    def __init__(self, nombre, edad, especie):
        self.nombre = nombre
        self.edad = edad
        self.especie = especie

    def amamantar(self):
        return f"{self.nombre} está amamantando a sus crías."   