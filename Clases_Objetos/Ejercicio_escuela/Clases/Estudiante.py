from Clases import Persona as p

class Estudiante(p.Persona):
    def __init__(self,nombre,edad,grado):
        super().__init__(nombre,edad)
        self.grado=grado
    
    def mostrar_grado(self):
        return f"Estoy en el grado {self.grado}"
