class Ciudades():
    def __init__(self):
        self.cabecera = None

    def insertar(self, nuevoNodo):
        aux = self.cabecera
        if(self.cabecera == None):
            self.cabecera = nuevoNodo
            return
        if(aux.siguiente!=None):
            aux = aux.siguiente
        aux.siguiente = nuevoNodo
        return
    