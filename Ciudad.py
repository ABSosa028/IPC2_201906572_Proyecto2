import  os, sys
import webbrowser
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

    def mostrar(self):
        webbrowser.open('matriz_{}.pdf'.format(self.nombre))

    #mostrar las posiciones de un archivo txt que contengan M
    def mostrarM(self):
        file = open("{}.txt".format(self.nombre), "r")
        fila = 1
        nMision = 0
        for line in file:
            columna = 1
            for letra in line:
                if letra == "C":
                    nMision += 1 
                    print("{}. Mision de Rescate a Civiles        Fila: {} Columna: {}".format(nMision, fila, columna))
                elif letra == "R":
                    nMision += 1 
                    print("{}. Mision de Extraccion de Recursos   Fila: {} Columna: {}".format(nMision, fila, columna))
                elif letra == "M":
                    nMision += 1 
                    print("{}. Mision de Quitar Militares         Fila: {} Columna: {}".format(nMision, fila, columna))

                columna = columna + 1
            fila = fila + 1
                
 

    def getnombre(self):
        return self.nombre
        