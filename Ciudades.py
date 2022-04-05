import os, sys
import webbrowser
from PIL import Image

class Ciudades():
    def __init__(self):
        self.cabecera = None

    def buscarNodo(self, id):
        yy = 1
        aux = self.cabecera
        while aux != None:
            if(yy == int(id)):
                return aux
            aux = aux.siguiente
            yy = yy + 1
        return None


    def insertar(self, nuevoNodo):
        aux = self.cabecera
        if(self.cabecera == None):
            self.cabecera = nuevoNodo
            return
        while(aux.siguiente!=None):
            aux = aux.siguiente
        aux.siguiente = nuevoNodo
        return
    
    def mostrar2(self):
        file = open("Reporte.dot","w")
        file.write("digraph G {node [fontname=\"Arial\"];node_A [shape=record    label=\"")

        p = self.cabecera
        i = 1
        file.write("{"+'numero'+"|")
        while p != None:
            file.write(str(i))
            i = i + 1
            p = p.siguiente
            if p != None:
                file.write("|")
        file.write("}|")

        auxi = self.cabecera
        s = 1

        file.write("{"+'ciudad'+"|")
        while auxi != None:
            file.write(auxi.getnombre())
            auxi = auxi.siguiente
            if auxi != None:
                file.write("|")            
        file.write("}")
   
        file.write("\"];} ")
        file.close()
        os.system("dot -Tpdf Reporte.dot -o Ciudades.pdf")
        webbrowser.open('Ciudades.pdf')

    def mostrar(self):
        aux = self.cabecera
        while aux != None:
            print(aux.nombre)
            aux = aux.siguiente
        return

    def enliztar(self):
        yy= 1
        aux = self.cabecera
        while aux != None:
            print(str(yy)+" "+aux.nombre)
            aux = aux.siguiente
            yy+=1
        return