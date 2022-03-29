class Robot():

    def __init__(self,codigo, nombre, tipo, capacidad, disponibilidad):
        self.codigo = codigo
        self.nombre = nombre
        self.tipo = tipo
        self.capacidad = capacidad
        self.disponibilidad = disponibilidad
        self.siguiente = None

    def usar(self):
        self.disponibilidad = 0

    def devolver(self):
        self.disponibilidad = 1
        