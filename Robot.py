class Robot():

    def __init__(self,codigo, nombre, tipo, capacidad, disponibilidad):
        self.codigo = codigo
        self.nombre = nombre
        self.tipo = tipo
        self.capacidad = capacidad
        self.disponibilidad = disponibilidad
        self.siguiente = None

    def getPoder(self):
        return self.capacidad
    
    def getCapacidad(self):
        return self.capacidad
    
    def setPoder(self, poder):
        self.capacidad = poder

    def usar(self):
        self.disponibilidad = 0
    
    def setDisponibilidad(self, disponibilidad):
        self.disponibilidad = disponibilidad
    
    def getDisponibilidad(self):
        return self.disponibilidad
    
    def getCodigo(self):
        return self.codigo

    def getNombre(self):
        return self.nombre
    
    def getNombreCodigo(self):
        return self.codigo + " " + self.nombre

    def devolver(self):
        self.disponibilidad = 1
    
    def getTipo(self):
        return self.tipo
        