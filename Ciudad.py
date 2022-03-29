
class Ciudad():
    def __init__(self, nombre, filas, columnas, casillas, militares):
        self.nombre = nombre
        self.casillas = casillas
        self.filas = filas
        self.columnas = columnas
        self.militares =militares
        self.siguiente = None

    def fil(self):
        return self.filas