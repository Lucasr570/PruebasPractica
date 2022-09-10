

class EstudianteClass:
    matricula = ""
    nombre = ""
    telefono = ""
    edad = ""
    peso = ""
    
    def __init__(self, matricula, nombre):
        self.matricula=matricula
        self.nombre=nombre
        
    def getMatricula(self):
        return self.matricula
    
    def getNombre(self):
        return self.nombre
    
    def getTelefono(self):
        return self.telefono
    
    def getEdad(self):
        return self.edad
    
    def getPeso(self):
        return self.peso
    
    def setNombre(self, nuevoNombre):
        self.nombre = nuevoNombre
        
    def setTelfono(self, nuevoTelefono):
        self.telefono = nuevoTelefono
        
    def setEdad(self, nuevaEdad):
        self.edad = nuevaEdad
        
    def setPeso(self, nuevoPeso):
        self.peso = nuevoPeso    
        
        
        
    
        
        
        
        
        
        