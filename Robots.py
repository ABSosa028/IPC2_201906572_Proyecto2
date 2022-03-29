import re


class Robots():
    def __init__(self) :
        self.primero = None

    def insert(self, nuevoNodo):
        aux = self.primero
        if(self.primero == None):
            self.primero = nuevoNodo
            return
        if(aux.siguiente !=None):
            aux = aux.siguiente
        aux.siguiente = nuevoNodo
        return    