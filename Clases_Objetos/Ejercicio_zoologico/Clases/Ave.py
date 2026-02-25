class Ave:
    def __init__(self, nombre, edad, especie):
        self.nombre = nombre
        self.edad = edad
        self.especie = especie

    def volar(self):
        return f"{self.nombre} está volando por el cielo."