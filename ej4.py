class Alumnos():
    def __innit__ (self, nombre,nota):
        self.nombre = nombre
        self.nota = nota 
    def __str__ (self):
        return 'nombre del alumno {}, nota del alumno {}'



class alumnosprimero (Alumnos): 
    def __init__ (self, nombre, nota, llevangafas):
        Alumnos().__init__(self,nombre, nota)
        self.llevangafas = llevangafas
        
    def __str__ (self):
            return 'nombre del alumno {}, nota del alumno {}, lleva gafas {}'



Alumno1 = alumnosprimero ('Juan', 7, 'SI')
Alumno2 = alumnosprimero ('Carla',2, 'NO')