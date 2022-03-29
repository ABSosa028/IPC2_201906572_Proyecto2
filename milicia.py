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
    
    

