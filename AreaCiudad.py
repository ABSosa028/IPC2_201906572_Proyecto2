from cuadro import Cuadro as dt
import sys,os
from PIL import Image
import webbrowser

class AreaCiudad():

    def __init__(self):
        self.inicio = None

    def CrearMatriz(self,n,m,Datos):
        q = None
        s = None
        k = 0
        for i in range(1,int(n)+1):
            for j in range(1,int(m)+1):
                nuevoNodo = dt(Datos[k],k)
                k = k + 1
                nuevoNodo.siguiente = None
                nuevoNodo.abajo = None
                if j == 1:
                    nuevoNodo.anterior = None
                    if self.inicio == None:
                        self.inicio = nuevoNodo
                    q = nuevoNodo
                else:
                    nuevoNodo.anterior = q
                    q.siguiente = nuevoNodo
                    q = nuevoNodo
                if i == 1:
                    nuevoNodo.arriba = None
                    q = nuevoNodo
                else:
                    nuevoNodo.arriba = s
                    s.abajo = nuevoNodo
                    s = s.siguiente
            s = self.inicio
            while s.abajo != None:
                s = s.abajo

    def MostrarMat(self):
        if self.inicio != None:
            aux = self.inicio
            while aux != None:
                auxi = aux
                while auxi != None:
                    auxi.Mostrar()
                    auxi = auxi.siguiente
                aux = aux.abajo
                print("")

    def LimpiarMat(self):
        if self.inicio != None:
            aux = self.inicio
            while aux != None:
                auxi = aux
                while auxi != None:
                    aux2 = auxi
                    auxi = auxi.siguiente
                    aux2 = None    
                aux3 = aux
                aux = aux.abajo
                aux3 = None
                print("")

    def imagen2(self,nombre):
        file = open("Reporte2.dot","w")
        file.write("digraph G {node [fontname=\"Arial\"];node_A [shape=record    label=\"")

        p = self.inicio
        i = 1
        file.write("{"+str(nombre)+" mod |")
        while p != None:
            file.write(str(i))
            i = i + 1
            p = p.abajo
            if p != None:
                file.write("|")
        file.write("}|")

        aux = self.inicio
        s = 1
        while aux != None:
            file.write("{"+str(s)+"|")
            auxi = aux
            while auxi != None:
                file.write(auxi.getDato())
                auxi = auxi.abajo
                if auxi != None:
                    file.write("|")
            aux = aux.siguiente
            file.write("}")
            s = s + 1
            if aux != None:
                file.write("|")
   
        file.write("\"];} ")
        file.close()
        os.system("dot -Tpng Reporte2.dot -o "+str(nombre)+"mod.png")
        im = Image.open(str(nombre)+"mod.png")
        im.show()

    def imagen(self, nombre):
        #-- lo primero es settear los valores que nos preocupan
        grafo = 'digraph T{ \nnode[shape=box fontname="Arial" fillcolor="white" style=filled ]'
        grafo += '\nroot[label = \"capa: ' +'\", group=1]\n'
        grafo += '''label = "{}" \nfontname="Arial Black" \nfontsize="15pt" \n
                    \n'''.format('MATRIZ DISPERSA')

        aux = self.inicio
        s = 1
        while aux != None:
            auxi = aux
            while auxi != None:
                auxi = auxi.abajo
                if auxi != None:
                    aux = aux.siguiente
            s = s + 1
            if aux != None:
                print('fui')


    def graficarDot(self, nombre):
        #-- lo primero es settear los valores que nos preocupan
        grafo = 'digraph T{ \nnode[shape=box fontname="Arial" fillcolor="white" style=filled ]'
        cont = 0
        auxiliar = self.inicio
        while auxiliar is not None:
            if auxiliar.siguiente is not None:
                grafo += 'C{}->C{}\n'.format(auxiliar.id, auxiliar.siguiente.id)
                grafo += 'C{}->C{}\n'.format(auxiliar.siguiente.id, auxiliar.id)
            cont += 1
            auxiliar = auxiliar.siguiente

        auxiliar = self.inicio
        aux = self.inicio
        #grafo += 'root->F{};\n root->C{};\n'.format(aux.id, auxiliar.id)
        #grafo += '{rank=same;root;'
        cont = 0
        auxiliar = self.inicio
        while auxiliar != None:
            #grafo += 'C{};'.format(auxiliar.id)
            cont += 1
            auxiliar = auxiliar.siguiente
        #grafo += '}\n'
        aux = self.inicio
        aux2 = aux.abajo
        cont = 0
        while aux != None:
            cont += 1
            while aux2 != None:
                #if aux2.caracter == '-':
                #    grafo += 'N{}_{}[label=" ",group="{}"];\n'.format(aux2.coordenadaX, aux2.coordenadaY, int(aux2.coordenadaY)+1)
                #el
                #if aux2.dato == '*':
                #    grafo += 'N{}_{}[label="{}",group="{}", fillcolor="black"];\n'.format(aux2.id, aux2.id, aux2.id, int(aux2.id)+1)          
                aux2 = aux2.siguiente
            aux = aux.siguiente
            if aux != None:
                aux2 = aux.abajo
        aux = self.inicio
        cont = 0
        while aux != None:
            cont = 0
            grafo += ''
            while aux2 != None:
                if aux2.siguiente != None:
                    grafo += 'N{}->N{};\n'.format(aux2.siguiente.id,  aux2.id)
                    grafo += 'N{}->N{};\n'.format(aux2.id,  aux2.siguiente.id)
                aux2 = aux2.siguiente
            aux = aux.abajo
        
        aux = self.inicio
        aux2 = aux.abajo
        cont = 0
        while aux != None:
            cont = 0
            grafo += ''
            while aux2 != None:
                if cont == 0:
                    #grafo += 'C{}->N{}_{};\n'.format(aux.id, aux2.id, aux2.id)
                    #grafo += 'N{}_{}->C{};\n'.format(aux2.id, aux2.id, aux.id) 
                    cont += 1
                if aux2.abajo != None:
                    grafo += 'N{}->N{};\n'.format(aux2.abajo.id,  aux2.id)
                    grafo += 'N{}->N{};\n'.format( aux2.id,  aux2.abajo.id)
                aux2 = aux2.abajo
            aux = aux.siguiente
            if aux != None:
                aux2 = aux.abajo
        grafo += '}'

        # ---- luego de crear el contenido del Dot, procedemos a colocarlo en un archivo
        dot = "matriz_{}_dot.txt".format(nombre)
        with open(dot, 'w') as f:
            f.write(grafo)
        result = "matriz_{}.pdf".format(nombre)
        os.system("dot -Tpdf " + dot + " -o " + result)
        webbrowser.open(result)