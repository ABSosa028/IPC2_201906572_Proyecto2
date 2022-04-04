#nodo mision con tipo mision y coordenadas
#from this import d


class Mision:
    def __init__(self, cod, tipo, nodoMis):
        self.cod = cod
        self.tipo = tipo 
        self.nodoMis = nodoMis
        self.siguiente = None

    def gettipo(self):
        return self.tipo

    def coordenadas(self): 
        return self.x,self.y

    def mostrar(self):
        if(self.tipo == "C"):
            a = ("Mision de Rescate a Civiles        Fila: {} Columna: {}".format(self.nodoMis.coordenadaX, self.nodoMis.coordenadaY))
        elif(self.tipo == "R"):
            a = ("Mision de Extraccion de Recursos   Fila: {} Columna: {}".format(self.nodoMis.coordenadaX, self.nodoMis.coordenadaY))
        print("{} {} {}".format(self.cod, self.tipo, a))
        return
    

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
    
    def mostrar(self):
        aux = self.primero
        while aux != None:
            if(aux.tipo == "C"):
                a = ("Mision de Rescate a Civiles        Fila: {} Columna: {}".format(aux.nodoMis.coordenadaX, aux.nodoMis.coordenadaY))
            elif(aux.tipo == "R"):
                a = ("Mision de Extraccion de Recursos   Fila: {} Columna: {}".format(aux.nodoMis.coordenadaX, aux.nodoMis.coordenadaY))
            print("{} {} {}".format(aux.cod, aux.tipo, a))
            aux = aux.siguiente
        return

    def buscarNodo(self,x):
        aux = self.primero
        while aux != None:
            if aux.cod == x:
                return aux
            aux = aux.siguiente
        return None