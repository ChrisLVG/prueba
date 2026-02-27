class Personaje:
    def __init__(self, nombre, fuerza,velocidad):
        self.nombre=nombre
        self.fuerza=fuerza
        self.velocidad=velocidad

    def __str__(self):
        return f"Personaje: {self.nombre}, Fuerza: {self.fuerza}, Velocidad: {self.velocidad}"
        
    def __add__(self, other):
        fuerza=(((self.fuerza + other.fuerza))/2)**2
        velocidad=(((self.velocidad + other.velocidad))/2)**2
        return Personaje(f"Equipo: {self.nombre}/{other.nombre}",fuerza,velocidad)




