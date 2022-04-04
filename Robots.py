import os, sys, webbrowser
from PIL import Image


class Robots():
    def __init__(self) :
        self.primero = None

    

    def insertar(self, nuevoNodo):
        aux = self.primero
        if(self.primero == None):
            self.primero = nuevoNodo
            return
        while(aux.siguiente!=None):
            aux = aux.siguiente
        aux.siguiente = nuevoNodo
        return  

    def buscarNodo(self, x):
        aux = self.primero
        while aux != None:
            if aux.codigo == x:
                return aux
            aux = aux.siguiente
        return None

    def mostrar2(self):
        file = open("Reporte.dot","w")
        file.write("digraph G {node [fontname=\"Arial\"];node_A [shape=record    label=\"")

        p = self.primero
        i = 1
        file.write("{"+'ID'+"|")
        while p != None:
            file.write(str(p.codigo))
            i = i + 1
            p = p.siguiente
            if p != None:
                file.write("|")
        file.write("}|")

        auxi = self.primero
        file.write("{"+'Nombre'+"|")
        while auxi != None:
            file.write(auxi.getNombre())
            auxi = auxi.siguiente
            if auxi != None:
                file.write("|")            
        file.write("}|")

        auxi = self.primero
        file.write("{"+'Tipo'+"|")
        while auxi != None:
            file.write(auxi.getTipo())
            auxi = auxi.siguiente
            if auxi != None:
                file.write("|")            
        file.write("}|")

        auxi = self.primero
        file.write("{"+'Capacidad Combate'+"|")
        while auxi != None:
            file.write(auxi.getCapacidad())
            auxi = auxi.siguiente
            if auxi != None:
                file.write("|")            
        file.write("}")
   
        file.write("\"];} ")
        file.close()
        os.system("dot -Tpdf Reporte.dot -o Robots.pdf")
        webbrowser.open('Robots.pdf')

    def mostrar(self):
        aux = self.primero
        while aux != None:
            print(aux.getNombreCodigo())
            aux = aux.siguiente
        return
    
    def enliztar(self, tp):
        if(tp=='C'):
            tp = 'ChapinRescue'
        elif(tp == 'R'):
            tp = 'ChapinFighter'
        aux = self.primero
        while aux != None:
            if(aux.getTipo() == tp):
                print('id:{}  {}  {}'.format(aux.codigo,aux.nombre,aux.tipo))
            aux = aux.siguiente
        return