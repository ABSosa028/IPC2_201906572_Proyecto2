#nodo mision con tipo mision y coordenadas
from this import d


class Mision:
    def __init__(self,tipo,x,y):
        self.tipo = tipo 
        self.x = x 
        self.y = y 
        self.siguiente = None

    def coordenadas(self): 
        return self.x,self.y

#lista de misiones
class ListaMisiones:
    
    def __init__(self):
        self.primero = None

    def insertar(self,nuevoNodo):
        aux = self.primero
        if(self.primero == None):
            self.primero = nuevoNodo
            return
        while(aux.siguiente!=None):
            aux = aux.siguiente
        aux.siguiente = nuevoNodo
        return
    
    def selectMision(self,x,y):
        aux = self.primero
        while aux != None:
            if aux.x == x and aux.y == y:
                return aux.tipo
            aux = aux.siguiente
        return None