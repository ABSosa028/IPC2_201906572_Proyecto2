import re


class Milicia():
    def __init__(self):
        self.primero = None

    def insert(self, military):
        aux = self.primero
        if(self.primero == None):
            self.primero = military
            return
        while(aux.siguiente != None):
            aux = aux.siguiente
        aux.siguiente = military
        return
    
    def buscarNodo(self, x, y):
        aux = self.primero
        while aux != None:
            if aux.positionx == x and aux.positiony == y:
                return aux
            aux = aux.siguiente
        return None
    
    

