import  os, sys
from PIL import Image

class Ciudad():
    def __init__(self, nombre, filas, columnas, casillas, militares):
        self.nombre = nombre
        self.casillas = casillas
        self.filas = filas
        self.columnas = columnas
        self.militares =militares
        self.siguiente = None

    def getfil(self):
        return self.filas

    def getnombre(self):
        return self.nombre
        