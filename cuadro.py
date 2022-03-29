class Cuadro():

    def __init__ (self,dato,id):
        self.id = id
        self.dato = dato
        self.siguiente = None
        self.anterior = None
        self.abajo = None
        self.arriba = None

    def Mostrar(self):
        print(str(self.dato), end = "")
        
    def getDato(self):

        return self.dato
    
    def setDato(self,dato):
        self.dato = dato