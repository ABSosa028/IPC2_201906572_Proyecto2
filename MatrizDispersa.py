import re
from sys import maxunicode
from Nodo_Encabezado import Nodo_Encabezado
from Lista_Encabezado import Lista_Encabezado
import os
import random
import webbrowser
from Mision import ListaMisiones as Misiones
from Mision import Mision as ms

# -----------------------------Codigo de MATRIZ DISPERSA ----------------
# -------- Clase NodoOrtogonal, con 4 apuntadores -> Nodos Internos

class Nodo_Interno(): # Nodos ortogonales
    def __init__(self, x, y, caracter):# 'caracter' puede ser cualquier valor
        self.caracter = caracter
        self.coordenadaX = x  # fila
        self.coordenadaY = y  # columna
        self.arriba = None
        self.abajo = None
        self.derecha = None  # self.siguiente
        self.izquierda = None  # self.anterior

    def Mostrar(self):
        print(str(self.caracter), end = "")
    
    def getCaracter(self):
        return self.caracter

    def setCaracter(self, caracter):
        self.caracter = caracter

class MatrizDispersa():
    def __init__(self, capa):
        self.capa = capa
        self.filas = Lista_Encabezado('fila')
        self.columnas = Lista_Encabezado('columna')

    def MostrarMat(self):
        if self.inicio != None:
            aux = self.inicio
            while aux != None:
                auxi = aux
                while auxi != None:
                    auxi.Mostrar()
                    auxi = auxi.derecha
                aux = aux.abajo
                print("")

    def MostrarMisiones(self):
        MisionesDisponibles = Misiones()
        contador_mis = 1
        if self.filas.primero.acceso != None:
            aux = self.filas.primero.acceso
            while aux != None:
                auxi = aux
                while auxi != None:
                    if( auxi.caracter == 'C'):
                        nuevaMis = ms(contador_mis, auxi.caracter, auxi)
                        contador_mis += 1
                        MisionesDisponibles.insertar(nuevaMis)
                    elif( auxi.caracter == 'R'):
                        nuevaMis = ms(contador_mis, auxi.caracter, auxi)
                        contador_mis += 1
                        MisionesDisponibles.insertar(nuevaMis)
                    auxi = auxi.derecha
                aux = aux.abajo
            return MisionesDisponibles

    def MostrarEntradas(self):
        EntradasDisponibles = Misiones()
        cont_entradas = 1
        if self.filas.primero.acceso != None:
            aux = self.filas.primero.acceso
            while aux != None:
                auxi = aux
                while auxi != None:
                    if( auxi.caracter == 'E'):
                        nuevaEntr = ms(cont_entradas, auxi.caracter, auxi)
                        cont_entradas += 1
                        EntradasDisponibles.insertar(nuevaEntr)
                    auxi = auxi.derecha
                aux = aux.abajo
            return EntradasDisponibles

    def mderecha(self, nodo):
        if(nodo.derecha.caracter != 'E' and nodo.derecha.caracter != 'C' and nodo.derecha.caracter != 'M'):
            nodo.derecha.setCaracter('W')
        return 
    
    def mizquierda(self, nodo):
        if(nodo.izquierda.caracter != 'E' and nodo.izquierda.caracter != 'C' and nodo.izquierda.caracter != 'M'):
            nodo.izquierda.setCaracter('W')
        return

    def mabajo(self, nodo):
        if(nodo.abajo.caracter != 'E' and nodo.abajo.caracter != 'C' and nodo.abajo.caracter != 'M'):
            nodo.abajo.setCaracter('W')
        return
    
    def marriba(self, nodo):
        if(nodo.arriba.caracter != 'E' and nodo.arriba.caracter != 'C' and nodo.arriba.caracter != 'M'):
            nodo.arriba.setCaracter('W')
        return
    
    def rderecha(self, nodo):
        if(nodo.derecha.caracter != 'E' and nodo.derecha.caracter != 'C' and nodo.derecha.caracter != 'M'):
            nodo.derecha.setCaracter(' ')
        return
    
    def rizquierda(self, nodo):
        if(nodo.izquierda.caracter != 'E' and nodo.izquierda.caracter != 'C' and nodo.izquierda.caracter != 'M'):
            nodo.izquierda.setCaracter(' ')
        return
    
    def rarriba(self, nodo):
        if(nodo.arriba.caracter != 'E' and nodo.arriba.caracter != 'C' and nodo.arriba.caracter != 'M'):
            nodo.arriba.setCaracter(' ')
        return
    
    def rabajo(self, nodo):
        if(nodo.abajo.caracter != 'E' and nodo.abajo.caracter != 'C' and nodo.abajo.caracter != 'M'):
            nodo.abajo.setCaracter(' ')   
        return

    #buscar camino matriz ortogonal
    def buscarCaminoRescate(self, inicio, fin):
        aux = inicio
        muvs = ['e']
        pas = ['E',' ','C','']
        hec = []
        contInt = 0
        while((inicio.coordenadaX != fin.coordenadaX) or (inicio.coordenadaY != fin.coordenadaY)):
            numero = int(random.randint(1, 4))
            #intentar muv 
            if(aux.derecha != None and numero ==1 ):
                if( aux.derecha.caracter in pas):
                    self.mderecha(aux)
                    muvs.append('r')
                    aux = aux.derecha
                    hec = []
                else:
                    hec.append('r')
            elif(aux.arriba != None and numero ==2):
                if( aux.arriba.caracter in pas ):
                    muvs.append('u')
                    self.marriba(aux)
                    hec = []
                    aux = aux.arriba
                else:
                    hec.append('u')
            elif(aux.abajo != None and numero ==3):
                if( aux.abajo.caracter in pas ):
                    self.mabajo(aux)
                    hec = []
                    aux = aux.abajo
                    muvs.append('d')
                else:
                    hec.append('d') 
            elif(aux.izquierda != None and numero ==4):
                if( aux.izquierda.caracter in pas ):
                    muvs.append('l')
                    hec = []
                    self.mizquierda(aux)
                else:
                    hec.append('l')
            if(aux.abajo == None or aux.arriba == None or aux.derecha == None or aux.izquierda == None):
                if('l' in hec and 'r' in hec and 'd' in hec and aux.arriba == None):
                    hec.append('u')
                if('l' in hec and 'r' in hec and 'u' in hec and aux.abajo == None):
                    hec.append('d')
                if('u' in hec and 'r' in hec and 'd' in hec and aux.derecha == None):
                    hec.append('l')
                if('l' in hec and 'u' in hec and 'd' in hec and aux.izquierda == None):
                    hec.append('r')
            if(aux.abajo != None or aux.arriba != None or aux.derecha != None or aux.izquierda != None):
                    if(aux.arriba != None and aux.caracter not in pas):
                        hec.append('u')
                    if(aux.abajo != None and aux.abajo.caracter not in pas ):
                        hec.append('d')
                    if(aux.izquierda != None and aux.izquierda.caracter not in pas):
                        hec.append('l')
                    if(aux.derecha != None and aux.derecha.caracter not in pas):
                        hec.append('r')
            else:
                if(aux.arriba == None):
                    hec.append('u')
                if(aux.abajo == None):
                    hec.append('d')
                if(aux.izquierda == None):
                    hec.append('l')
                if(aux.derecha == None):
                    hec.append('r')
            if('l' in hec and 'r' in hec and 'u' in hec and 'd' in hec):
                contInt +=1
                aux = inicio
                muvs = ['e']
                if self.filas.primero.acceso != None:
                    auxo = self.filas.primero.acceso
                    while auxo != None:
                        auxi = auxo
                        while auxi != None:
                            if(auxi.caracter == 'W'):
                                auxi.setCaracter(' ')
                            auxi = auxi.derecha
                        auxo = auxo.abajo    
                hec = []
            if(aux.abajo == fin or aux.arriba == fin or aux.derecha == fin or aux.izquierda == fin):
                print('--------------------------------------------------------------------------------')
                print('Mision Completada')
                return True
                print('--------------------------------------------------------------------------------')
                return 
            if(contInt > 200):
                print('--------------------------------------------------------------------------------')
                print('Mision no posible')
                print('--------------------------------------------------------------------------------')
                return False
            if(len(muvs)>250 or len(hec)>250):
                if ('l' not in hec or 'r' not in hec or 'u' not in hec or 'd' not in hec):
                    muvs = ['e']
                    aux = inicio
                    muvs = ['e']
                    if self.filas.primero.acceso != None:
                        auxo = self.filas.primero.acceso
                        while auxo != None:
                            auxi = auxo
                            while auxi != None:
                                if(auxi.caracter == 'W'):
                                    auxi.setCaracter(' ')
                                auxi = auxi.derecha
                            auxo = auxo.abajo    
                    hec = []
                    continue
                print('--------------------------------------------------------------------------------')
                print('Mision no posible ')
                print('--------------------------------------------------------------------------------')
                return False
        return False
        
    def buscarCaminoRecurso(self, inicio, fin, robot, milisia):
        aux = inicio
        muvs = ['e']
        contInt = 0
        pas = ['E',' ','C','M']
        hec = []
        vida = int(robot.getPoder())
        while(inicio.coordenadaX != fin.coordenadaX or inicio.coordenadaY != fin.coordenadaY):
            numero = int(random.randint(1, 4))

            #right
            if(aux.derecha != None and numero ==1 ):
                if( aux.derecha.caracter in pas):
                    if(aux.derecha.caracter == 'M'):
                        f = milisia.buscarNodo(aux.derecha.coordenadaX, aux.derecha.coordenadaY)
                        if(f != None):
                            if(int(f.getPoder()) < vida):
                                nP = vida-int(f.getPoder())
                                vida = nP
                                self.mderecha(aux)
                                muvs.append('r')
                                aux = aux.derecha
                                hec = []
                                continue
                            else:
                                hec.append('r')
                                continue
                    else:
                        self.mderecha(aux)
                        muvs.append('r')
                        aux = aux.derecha
                        hec = []
                else:
                    hec.append('r')
            #up
            elif(aux.arriba != None and numero ==2):
                if( aux.arriba.caracter in pas ):
                    if(aux.arriba.caracter == 'M'):
                        f = milisia.buscarNodo(aux.arriba.coordenadaX, aux.arriba.coordenadaY)
                        if(f != None):
                            if(int(f.getPoder()) < vida):
                                nP = vida-int(f.getPoder())
                                vida = nP
                                self.marriba(aux)
                                muvs.append('u')
                                aux = aux.arriba
                                hec = []
                                continue
                            else:
                                hec.append('u')
                                continue
                    else:
                        muvs.append('u')
                        self.marriba(aux)
                        hec = []
                        aux = aux.arriba
                else:
                    hec.append('u')
            #down
            elif(aux.abajo != None and numero ==3):
                if( aux.abajo.caracter in pas ):
                    if(aux.abajo.caracter == 'M'):
                        f = milisia.buscarNodo(aux.abajo.coordenadaX, aux.abajo.coordenadaY)
                        if(f != None):
                            if(int(f.getPoder()) < vida):
                                nP = vida-int(f.getPoder())
                                vida = nP
                                self.mabajo(aux)
                                muvs.append('d')
                                aux = aux.abajo
                                hec = []
                                continue
                            else:
                                hec.append('d')
                                continue
                    else:
                        self.mabajo(aux)
                        hec = []
                        aux = aux.abajo
                        muvs.append('d')
                else:
                    hec.append('d') 
            #left
            elif(aux.izquierda != None and numero ==4):
                if( aux.izquierda.caracter in pas ):
                    if(aux.izquierda.caracter == 'M'):
                        f = milisia.buscarNodo(aux.izquierda.coordenadaX, aux.izquierda.coordenadaY)
                        if(f != None):
                            if(int(f.getPoder()) < vida):
                                nP = vida-int(f.getPoder())
                                vida = nP
                                self.mizquierda(aux)
                                muvs.append('l')
                                aux = aux.izquierda
                                hec = []
                                continue
                            else:
                                hec.append('l')
                                continue
                    else:
                        muvs.append('l')
                        hec = []
                        self.mizquierda(aux)
                else:
                    hec.append('l')
            if(aux.abajo == None or aux.arriba == None or aux.derecha == None or aux.izquierda == None):
                if('l' in hec and 'r' in hec and 'd' in hec and aux.arriba == None):
                    hec.append('u')
                if('l' in hec and 'r' in hec and 'u' in hec and aux.abajo == None):
                    hec.append('d')
                if('u' in hec and 'r' in hec and 'd' in hec and aux.derecha == None):
                    hec.append('l')
                if('l' in hec and 'u' in hec and 'd' in hec and aux.izquierda == None):
                    hec.append('r')
            if(aux.abajo != None or aux.arriba != None or aux.derecha != None or aux.izquierda != None):
                    if(aux.arriba != None and aux.caracter not in pas):
                        hec.append('u')
                    if(aux.abajo != None and aux.abajo.caracter not in pas ):
                        hec.append('d')
                    if(aux.izquierda != None and aux.izquierda.caracter not in pas):
                        hec.append('l')
                    if(aux.derecha != None and aux.derecha.caracter not in pas):
                        hec.append('r')
            else:
                if(aux.arriba == None):
                    hec.append('u')
                if(aux.abajo == None):
                    hec.append('d')
                if(aux.izquierda == None):
                    hec.append('l')
                if(aux.derecha == None):
                    hec.append('r')
            if('l' in hec and 'r' in hec and 'u' in hec and 'd' in hec):
                contInt +=1
                aux = inicio
                muvs = ['e']
                if self.filas.primero.acceso != None:
                    auxo = self.filas.primero.acceso
                    while auxo != None:
                        auxi = auxo
                        while auxi != None:
                            if(auxi.caracter == 'W'):
                                auxi.setCaracter(' ')
                            auxi = auxi.derecha
                        auxo = auxo.abajo
                vida = int(robot.getPoder())    
                hec = []
            if(aux.abajo == fin or aux.arriba == fin or aux.derecha == fin or aux.izquierda == fin):
                print('--------------------------------------------------------------------------------')
                print('Mision Completada')
                misterRob = ('Robot utilizado: {} tipo:{} capacidad inicial {} capacidad final {}'.format(robot.getNombre(), robot.getTipo(), robot.getPoder(), vida))
                self.graficarRecorridoRec('Recursos' ,'x:{} y:{} \n {}'.format(fin.coordenadaX,fin.coordenadaY,misterRob ))
                return True
                print('--------------------------------------------------------------------------------')
                return 
            if(contInt > 200):
                print('--------------------------------------------------------------------------------')
                print('Mision no posible')
                print('--------------------------------------------------------------------------------')
                return False
            if(len(muvs)>250 or len(hec)>250):
                if ('l' not in hec or 'r' not in hec or 'u' not in hec or 'd' not in hec):
                    muvs = ['e']
                    aux = inicio
                    muvs = ['e']
                    if self.filas.primero.acceso != None:
                        auxo = self.filas.primero.acceso
                        while auxo != None:
                            auxi = auxo
                            while auxi != None:
                                if(auxi.caracter == 'W'):
                                    auxi.setCaracter(' ')
                                auxi = auxi.derecha
                            auxo = auxo.abajo    
                    vida = int(robot.getPoder())
                    hec = []
                    continue
                print('--------------------------------------------------------------------------------')
                print('Mision no posible 2')
                print('--------------------------------------------------------------------------------')
                return False
        return False
        
    def quitarW(self):
        if self.filas.primero.acceso != None:
            auxo = self.filas.primero.acceso
            while auxo != None:
                auxi = auxo
                while auxi != None:
                    if(auxi.caracter == 'W'):
                        auxi.setCaracter(' ')
                    auxi = auxi.derecha
                auxo = auxo.abajo 
            return   
    
    def insert(self, pos_x, pos_y, caracter):
        nuevo = Nodo_Interno(pos_x, pos_y, caracter) # se crea nodo interno
        # --- lo prinero sera buscar si ya existen los encabezados en la matriz
        nodo_X = self.filas.getEncabezado(pos_x)
        nodo_Y = self.columnas.getEncabezado(pos_y)

        if nodo_X == None: # --- comprobamos que el encabezado fila pos_x exista
             # --- si nodo_X es nulo, quiere decir que no existe encabezado fila pos_x
            nodo_X = Nodo_Encabezado(pos_x)
            self.filas.insertar_nodoEncabezado(nodo_X)

        if nodo_Y == None: # --- comprobamos que el encabezado columna pos_y exista
            # --- si nodo_Y es nulo, quiere decir que no existe encabezado columna pos_y
            nodo_Y = Nodo_Encabezado(pos_y)
            self.columnas.insertar_nodoEncabezado(nodo_Y)

        # ----- INSERTAR NUEVO EN FILA
        if nodo_X.acceso == None: # -- comprobamos que el nodo_x no esta apuntando hacia ningun nodoInterno
            nodo_X.acceso = nuevo
        else: # -- si esta apuntando, validamos si la posicion de la columna del NUEVO nodoInterno es menor a la posicion de la columna del acceso 
            if nuevo.coordenadaY < nodo_X.acceso.coordenadaY: # F1 --->  NI 1,1     NI 1,3
                nuevo.derecha = nodo_X.acceso              
                nodo_X.acceso.izquierda = nuevo
                nodo_X.acceso = nuevo
            else:
                #de no cumplirse debemos movernos de izquierda a derecha buscando donde posicionar el NUEVO nodoInterno
                tmp : Nodo_Interno = nodo_X.acceso     # nodo_X:F1 --->      NI 1,2; NI 1,3; NI 1,5;
                while tmp != None:                      #NI 1,6
                    if nuevo.coordenadaY < tmp.coordenadaY:
                        nuevo.derecha = tmp
                        nuevo.izquierda = tmp.izquierda
                        tmp.izquierda.derecha = nuevo
                        tmp.izquierda = nuevo
                        break;
                    elif nuevo.coordenadaX == tmp.coordenadaX and nuevo.coordenadaY == tmp.coordenadaY: #validamos que no haya repetidas
                        break;
                    else:
                        if tmp.derecha == None:
                            tmp.derecha = nuevo
                            nuevo.izquierda = tmp
                            break;
                        else:
                            tmp = tmp.derecha 
                             #         nodo_Y:        C1    C3      C5      C6
                             # nodo_X:F1 --->      NI 1,2; NI 1,3; NI 1,5; NI 1,6;
                             # nodo_X:F2 --->      NI 2,2; NI 2,3; NI 2,5; NI 2,6;

        # ----- INSERTAR NUEVO EN COLUMNA
        if nodo_Y.acceso == None:  # -- comprobamos que el nodo_y no esta apuntando hacia ningun nodoCelda
            nodo_Y.acceso = nuevo
        else: # -- si esta apuntando, validamos si la posicion de la fila del NUEVO nodoCelda es menor a la posicion de la fila del acceso 
            if nuevo.coordenadaX < nodo_Y.acceso.coordenadaX:
                nuevo.abajo = nodo_Y.acceso
                nodo_Y.acceso.arriba = nuevo
                nodo_Y.acceso = nuevo
            else:
                # de no cumplirse, debemos movernos de arriba hacia abajo buscando donde posicionar el NUEVO
                tmp2 : Nodo_Interno = nodo_Y.acceso
                while tmp2 != None:
                    if nuevo.coordenadaX < tmp2.coordenadaX:
                        nuevo.abajo = tmp2
                        nuevo.arriba = tmp2.arriba
                        tmp2.arriba.abajo = nuevo
                        tmp2.arriba = nuevo
                        break;
                    elif nuevo.coordenadaX == tmp2.coordenadaX and nuevo.coordenadaY == tmp2.coordenadaY: #validamos que no haya repetidas
                        break;
                    else:
                        if tmp2.abajo == None:
                            tmp2.abajo = nuevo
                            nuevo.arriba = tmp2
                            break
                        else:
                            tmp2 = tmp2.abajo

    def graficarDibujo(self,nombre):
        contenido = '''digraph G{
    node[shape=box, width=0.7, height=0.7, fontname="Arial", fillcolor="white", style=filled]
    edge[style = "bold"]
    node[label = "''' + str(nombre) +'''" fillcolor="darkolivegreen1" pos = "-1,1!"]raiz;'''
        contenido += '''label = "{}" \nfontname="Arial Black" \nfontsize="25pt" \n
                    \n'''.format('\nMATRIZ '+str(nombre).upper())
                    


        # --graficar nodos ENCABEZADO
        # --graficar nodos fila
        pivote = self.filas.primero
        posx = 0
        while pivote != None:
            contenido += '\n\tnode[label = "F{}" fillcolor="azure3" pos="-1,-{}!" shape=box]x{};'.format(pivote.id, 
            posx, pivote.id)
            pivote = pivote.siguiente
            posx += 1
        pivote = self.filas.primero
        while pivote.siguiente != None:
            contenido += '\n\tx{}->x{};'.format(pivote.id, pivote.siguiente.id)
            contenido += '\n\tx{}->x{}[dir=back];'.format(pivote.id, pivote.siguiente.id)
            pivote = pivote.siguiente
        contenido += '\n\traiz->x{};'.format(self.filas.primero.id)

        # --graficar nodos columna
        pivotey = self.columnas.primero
        posy = 0
        while pivotey != None:
            contenido += '\n\tnode[label = "C{}" fillcolor="azure3" pos = "{},1!" shape=box]y{};'.format(pivotey.id, 
            posy, pivotey.id)
            pivotey = pivotey.siguiente
            posy += 1
        pivotey = self.columnas.primero
        while pivotey.siguiente != None:
            contenido += '\n\ty{}->y{};'.format(pivotey.id, pivotey.siguiente.id)
            contenido += '\n\ty{}->y{}[dir=back];'.format(pivotey.id, pivotey.siguiente.id)
            pivotey = pivotey.siguiente
        contenido += '\n\traiz->y{};'.format(self.columnas.primero.id)

        #ya con las cabeceras graficadas, lo siguiente es los nodos internos, o nodosCelda
        pivote = self.filas.primero
        posx = 0
        while pivote != None:
            pivote_celda : Nodo_Interno = pivote.acceso
            while pivote_celda != None:
                # --- buscamos posy
                pivotey = self.columnas.primero
                posy_celda = 0
                while pivotey != None:
                    if pivotey.id == pivote_celda.coordenadaY: break
                    posy_celda += 1
                    pivotey = pivotey.siguiente
                if pivote_celda.caracter == '*':
                    contenido += '\n\tnode[label="*" fillcolor="black" pos="{},-{}!" shape=box]i{}_{};'.format( #pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    )
                elif pivote_celda.caracter == 'E':
                    contenido += '\n\tnode[label="E" fillcolor="green" pos="{},-{}!" shape=box]i{}_{};'.format( #pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    )
                elif pivote_celda.caracter == 'R':
                    contenido += '\n\tnode[label="R" fillcolor="gray" pos="{},-{}!" shape=box]i{}_{};'.format( #pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    )
                elif pivote_celda.caracter == 'C':
                    contenido += '\n\tnode[label="C" fillcolor="cyan" pos="{},-{}!" shape=box]i{}_{};'.format( #pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    )
                elif pivote_celda.caracter == 'M':
                    contenido += '\n\tnode[label="M" fillcolor="red" pos="{},-{}!" shape=box]i{}_{};'.format( #pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    )
                else:
                    contenido += '\n\tnode[label=" " fillcolor="white" pos="{},-{}!" shape=box]i{}_{};'.format( # pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    ) 
                pivote_celda = pivote_celda.derecha
            
            pivote_celda = pivote.acceso
            while pivote_celda != None:
                if pivote_celda.derecha != None:
                    contenido += '\n\ti{}_{}->i{}_{};'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY,
                    pivote_celda.derecha.coordenadaX, pivote_celda.derecha.coordenadaY)
                    contenido += '\n\ti{}_{}->i{}_{}[dir=back];'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY,
                    pivote_celda.derecha.coordenadaX, pivote_celda.derecha.coordenadaY)
                pivote_celda = pivote_celda.derecha
        
            contenido += '\n\tx{}->i{}_{};'.format(pivote.id, pivote.acceso.coordenadaX, pivote.acceso.coordenadaY)
            contenido += '\n\tx{}->i{}_{}[dir=back];'.format(pivote.id, pivote.acceso.coordenadaX, pivote.acceso.coordenadaY)
            pivote = pivote.siguiente
            posx += 1
        
        pivote = self.columnas.primero
        while pivote != None:
            pivote_celda : Nodo_Interno = pivote.acceso
            while pivote_celda != None:
                if pivote_celda.abajo != None:
                    contenido += '\n\ti{}_{}->i{}_{};'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY,
                    pivote_celda.abajo.coordenadaX, pivote_celda.abajo.coordenadaY)
                    contenido += '\n\ti{}_{}->i{}_{}[dir=back];'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY,
                    pivote_celda.abajo.coordenadaX, pivote_celda.abajo.coordenadaY) 
                pivote_celda = pivote_celda.abajo
            contenido += '\n\ty{}->i{}_{};'.format(pivote.id, pivote.acceso.coordenadaX, pivote.acceso.coordenadaY)
            contenido += '\n\ty{}->i{}_{}[dir=back];'.format(pivote.id, pivote.acceso.coordenadaX, pivote.acceso.coordenadaY)
            pivote = pivote.siguiente
                
        contenido += '\n}'
        #--- se genera DOT y se procede a ecjetuar el comando
        dot = "matriz_{}_dot.txt".format(nombre)
        with open(dot, 'w') as grafo:
            grafo.write(contenido)
        result = "matriz_{}.pdf".format(nombre)
        os.system("neato -Tpdf " + dot + " -o " + result)

    def graficarRecorrido(self,nombre):
        contenido = '''digraph G{
    node[shape=box, width=0.7, height=0.7, fontname="Arial", fillcolor="white", style=filled]
    edge[style = "bold"]
    node[label = "''' + str(nombre) +'''" fillcolor="darkolivegreen1" pos = "-1,1!"]raiz;'''
        contenido += '''label = "{}" \nfontname="Arial Black" \nfontsize="25pt" \n
                    \n'''.format('\nMATRIZ '+str(nombre).upper())
                    


        # --graficar nodos ENCABEZADO
        # --graficar nodos fila
        pivote = self.filas.primero
        posx = 0
        while pivote != None:
            contenido += '\n\tnode[label = "F{}" fillcolor="azure3" pos="-1,-{}!" shape=box]x{};'.format(pivote.id, 
            posx, pivote.id)
            pivote = pivote.siguiente
            posx += 1
        pivote = self.filas.primero
        while pivote.siguiente != None:
            contenido += '\n\tx{}->x{};'.format(pivote.id, pivote.siguiente.id)
            contenido += '\n\tx{}->x{}[dir=back];'.format(pivote.id, pivote.siguiente.id)
            pivote = pivote.siguiente
        contenido += '\n\traiz->x{};'.format(self.filas.primero.id)

        # --graficar nodos columna
        pivotey = self.columnas.primero
        posy = 0
        while pivotey != None:
            contenido += '\n\tnode[label = "C{}" fillcolor="azure3" pos = "{},1!" shape=box]y{};'.format(pivotey.id, 
            posy, pivotey.id)
            pivotey = pivotey.siguiente
            posy += 1
        pivotey = self.columnas.primero
        while pivotey.siguiente != None:
            contenido += '\n\ty{}->y{};'.format(pivotey.id, pivotey.siguiente.id)
            contenido += '\n\ty{}->y{}[dir=back];'.format(pivotey.id, pivotey.siguiente.id)
            pivotey = pivotey.siguiente
        contenido += '\n\traiz->y{};'.format(self.columnas.primero.id)

        #ya con las cabeceras graficadas, lo siguiente es los nodos internos, o nodosCelda
        pivote = self.filas.primero
        posx = 0
        while pivote != None:
            pivote_celda : Nodo_Interno = pivote.acceso
            while pivote_celda != None:
                # --- buscamos posy
                pivotey = self.columnas.primero
                posy_celda = 0
                while pivotey != None:
                    if pivotey.id == pivote_celda.coordenadaY: break
                    posy_celda += 1
                    pivotey = pivotey.siguiente
                if pivote_celda.caracter == '*':
                    contenido += '\n\tnode[label="*" fillcolor="black" pos="{},-{}!" shape=box]i{}_{};'.format( #pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    )
                elif pivote_celda.caracter == 'E':
                    contenido += '\n\tnode[label="E" fillcolor="green" pos="{},-{}!" shape=box]i{}_{};'.format( #pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    )
                elif pivote_celda.caracter == 'R':
                    contenido += '\n\tnode[label="R" fillcolor="gray" pos="{},-{}!" shape=box]i{}_{};'.format( #pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    )
                elif pivote_celda.caracter == 'C':
                    contenido += '\n\tnode[label="C" fillcolor="cyan" pos="{},-{}!" shape=box]i{}_{};'.format( #pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    )
                elif pivote_celda.caracter == 'M':
                    contenido += '\n\tnode[label="M" fillcolor="red" pos="{},-{}!" shape=box]i{}_{};'.format( #pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    )
                elif pivote_celda.caracter == 'W':
                    contenido += '\n\tnode[label=" " fillcolor="yellow" pos="{},-{}!" shape=box]i{}_{};'.format( #pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    )
                else:
                    contenido += '\n\tnode[label=" " fillcolor="white" pos="{},-{}!" shape=box]i{}_{};'.format( # pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    ) 
                pivote_celda = pivote_celda.derecha
            
            pivote_celda = pivote.acceso
            while pivote_celda != None:
                if pivote_celda.derecha != None:
                    contenido += '\n\ti{}_{}->i{}_{};'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY,
                    pivote_celda.derecha.coordenadaX, pivote_celda.derecha.coordenadaY)
                    contenido += '\n\ti{}_{}->i{}_{}[dir=back];'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY,
                    pivote_celda.derecha.coordenadaX, pivote_celda.derecha.coordenadaY)
                pivote_celda = pivote_celda.derecha
        
            contenido += '\n\tx{}->i{}_{};'.format(pivote.id, pivote.acceso.coordenadaX, pivote.acceso.coordenadaY)
            contenido += '\n\tx{}->i{}_{}[dir=back];'.format(pivote.id, pivote.acceso.coordenadaX, pivote.acceso.coordenadaY)
            pivote = pivote.siguiente
            posx += 1
        
        pivote = self.columnas.primero
        while pivote != None:
            pivote_celda : Nodo_Interno = pivote.acceso
            while pivote_celda != None:
                if pivote_celda.abajo != None:
                    contenido += '\n\ti{}_{}->i{}_{};'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY,
                    pivote_celda.abajo.coordenadaX, pivote_celda.abajo.coordenadaY)
                    contenido += '\n\ti{}_{}->i{}_{}[dir=back];'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY,
                    pivote_celda.abajo.coordenadaX, pivote_celda.abajo.coordenadaY) 
                pivote_celda = pivote_celda.abajo
            contenido += '\n\ty{}->i{}_{};'.format(pivote.id, pivote.acceso.coordenadaX, pivote.acceso.coordenadaY)
            contenido += '\n\ty{}->i{}_{}[dir=back];'.format(pivote.id, pivote.acceso.coordenadaX, pivote.acceso.coordenadaY)
            pivote = pivote.siguiente
                
        contenido += '\n}'
        #--- se genera DOT y se procede a ecjetuar el comando
        dot = "matriz_{}_dot.txt".format(nombre)
        with open(dot, 'w') as grafo:
            grafo.write(contenido)
        result = "matriz_{}.pdf".format(nombre)
        os.system("neato -Tpdf " + dot + " -o " + result)

    def graficarDot(self, nombre):
        #-- lo primero es settear los valores que nos preocupan
        grafo = 'digraph T{ \nnode[shape=box fontname="Arial" fillcolor="white" style=filled ]'
        grafo += '\nroot[label = \"capa: '+ str(self.capa) +'\", group=1]\n'
        grafo += '''label = "{}" \nfontname="Arial Black" \nfontsize="15pt" \n
                    \n'''.format('MATRIZ DISPERSA')

        # --- lo siguiente es escribir los nodos encabezados, empezamos con las filas, los nodos tendran el foramto Fn
        x_fila = self.filas.primero
        while x_fila != None:
            grafo += 'F{}[label="F{}",fillcolor="plum",group=1];\n'.format(x_fila.id, x_fila.id)
            x_fila = x_fila.siguiente

        # --- apuntamos los nodos F entre ellos
        x_fila = self.filas.primero
        while x_fila != None:
            if x_fila.siguiente != None:
                grafo += 'F{}->F{};\n'.format(x_fila.id, x_fila.siguiente.id)
                grafo += 'F{}->F{};\n'.format(x_fila.siguiente.id, x_fila.id)
            x_fila = x_fila.siguiente

        # --- Luego de los nodos encabezados fila, seguimos con las columnas, los nodos tendran el foramto Cn
        y_columna = self.columnas.primero
        while y_columna != None:
            group = int(y_columna.id)+1
            grafo += 'C{}[label="C{}",fillcolor="powderblue",group={}];\n'.format(y_columna.id, y_columna.id, str(group))
            y_columna = y_columna.siguiente
        
        # --- apuntamos los nodos C entre ellos
        cont = 0
        y_columna = self.columnas.primero
        while y_columna is not None:
            if y_columna.siguiente is not None:
                grafo += 'C{}->C{}\n'.format(y_columna.id, y_columna.siguiente.id)
                grafo += 'C{}->C{}\n'.format(y_columna.siguiente.id, y_columna.id)
            cont += 1
            y_columna = y_columna.siguiente

        # --- luego que hemos escrito todos los nodos encabezado, apuntamos el nodo root hacua ellos 
        y_columna = self.columnas.primero
        x_fila = self.filas.primero
        grafo += 'root->F{};\n root->C{};\n'.format(x_fila.id, y_columna.id)
        grafo += '{rank=same;root;'
        cont = 0
        y_columna = self.columnas.primero
        while y_columna != None:
            grafo += 'C{};'.format(y_columna.id)
            cont += 1
            y_columna = y_columna.siguiente
        grafo += '}\n'
        aux = self.filas.primero
        aux2 = aux.acceso
        cont = 0
        while aux != None:
            cont += 1
            while aux2 != None:
                #if aux2.caracter == '-':
                #    grafo += 'N{}_{}[label=" ",group="{}"];\n'.format(aux2.coordenadaX, aux2.coordenadaY, int(aux2.coordenadaY)+1)
                #el
                if aux2.caracter == '*':
                    grafo += 'N{}_{}[label="{}",group="{}", fillcolor="gray"];\n'.format(aux2.coordenadaX, aux2.coordenadaY, aux2.caracter, int(aux2.coordenadaY)+1)          
                elif aux2.caracter == 'E':
                    grafo += 'N{}_{}[label="{}",group="{}", fillcolor="green"];\n'.format(aux2.coordenadaX, aux2.coordenadaY, aux2.caracter, int(aux2.coordenadaY)+1)          
                elif aux2.caracter == 'C':
                    grafo += 'N{}_{}[label="{}",group="{}", fillcolor="cyan"];\n'.format(aux2.coordenadaX, aux2.coordenadaY, aux2.caracter, int(aux2.coordenadaY)+1)          
                elif aux2.caracter == 'R':
                    grafo += 'N{}_{}[label="{}",group="{}", fillcolor="gray"];\n'.format(aux2.coordenadaX, aux2.coordenadaY, aux2.caracter, int(aux2.coordenadaY)+1)          
                aux2 = aux2.derecha
            aux = aux.siguiente
            if aux != None:
                aux2 = aux.acceso
        aux = self.filas.primero
        aux2 = aux.acceso
        cont = 0
        while aux is not None:
            rank = '{'+f'rank = same;F{aux.id};'
            cont = 0
            while aux2 != None:
                if cont == 0:
                    grafo += 'F{}->N{}_{};\n'.format(aux.id, aux2.coordenadaX, aux2.coordenadaY)
                    grafo += 'N{}_{}->F{};\n'.format(aux2.coordenadaX, aux2.coordenadaY, aux.id)
                    cont += 1
                if aux2.derecha != None:
                    grafo += 'N{}_{}->N{}_{};\n'.format(aux2.coordenadaX, aux2.coordenadaY, aux2.derecha.coordenadaX, aux2.derecha.coordenadaY)
                    grafo += 'N{}_{}->N{}_{};\n'.format(aux2.derecha.coordenadaX, aux2.derecha.coordenadaY, aux2.coordenadaX, aux2.coordenadaY)

                rank += 'N{}_{};'.format(aux2.coordenadaX, aux2.coordenadaY)
                aux2 = aux2.derecha
            aux = aux.siguiente
            if aux != None:
                aux2 = aux.acceso
            grafo += rank+'}\n'
        aux = self.columnas.primero
        aux2 = aux.acceso
        cont = 0
        while aux != None:
            cont = 0
            grafo += ''
            while aux2 != None:
                if cont == 0:
                    grafo += 'C{}->N{}_{};\n'.format(aux.id, aux2.coordenadaX, aux2.coordenadaY)
                    grafo += 'N{}_{}->C{};\n'.format(aux2.coordenadaX, aux2.coordenadaY, aux.id) 
                    cont += 1
                if aux2.abajo != None:
                    grafo += 'N{}_{}->N{}_{};\n'.format(aux2.abajo.coordenadaX, aux2.abajo.coordenadaY, aux2.coordenadaX, aux2.coordenadaY)
                    grafo += 'N{}_{}->N{}_{};\n'.format( aux2.coordenadaX, aux2.coordenadaY,aux2.abajo.coordenadaX, aux2.abajo.coordenadaY)
                aux2 = aux2.abajo
            aux = aux.siguiente
            if aux != None:
                aux2 = aux.acceso
        grafo += '}'

        # ---- luego de crear el contenido del Dot, procedemos a colocarlo en un archivo
        dot = "matriz_{}_dot.txt".format(nombre)
        with open(dot, 'w') as f:
            f.write(grafo)
        result = "matriz_{}.pdf".format(nombre)
        os.system("dot -Tpdf " + dot + " -o " + result)

    def graficarRecorridoRec(self,nombre, datos):
        contenido = '''digraph G{
    node[shape=box, width=0.7, height=0.7, fontname="Arial", fillcolor="white", style=filled]
    edge[style = "bold"]
    node[label = "''' + str(nombre) +'''" fillcolor="darkolivegreen1" pos = "-1,1!"]raiz;'''
        contenido += '''label = "{} \n {}" \nfontname="Arial Black" \nfontsize="25pt" \n
                    \n'''.format(('\nMATRIZ '+str(nombre).upper()),str(datos).upper())
                    


        # --graficar nodos ENCABEZADO
        # --graficar nodos fila
        pivote = self.filas.primero
        posx = 0
        while pivote != None:
            contenido += '\n\tnode[label = "F{}" fillcolor="azure3" pos="-1,-{}!" shape=box]x{};'.format(pivote.id, 
            posx, pivote.id)
            pivote = pivote.siguiente
            posx += 1
        pivote = self.filas.primero
        while pivote.siguiente != None:
            contenido += '\n\tx{}->x{};'.format(pivote.id, pivote.siguiente.id)
            contenido += '\n\tx{}->x{}[dir=back];'.format(pivote.id, pivote.siguiente.id)
            pivote = pivote.siguiente
        contenido += '\n\traiz->x{};'.format(self.filas.primero.id)

        # --graficar nodos columna
        pivotey = self.columnas.primero
        posy = 0
        while pivotey != None:
            contenido += '\n\tnode[label = "C{}" fillcolor="azure3" pos = "{},1!" shape=box]y{};'.format(pivotey.id, 
            posy, pivotey.id)
            pivotey = pivotey.siguiente
            posy += 1
        pivotey = self.columnas.primero
        while pivotey.siguiente != None:
            contenido += '\n\ty{}->y{};'.format(pivotey.id, pivotey.siguiente.id)
            contenido += '\n\ty{}->y{}[dir=back];'.format(pivotey.id, pivotey.siguiente.id)
            pivotey = pivotey.siguiente
        contenido += '\n\traiz->y{};'.format(self.columnas.primero.id)

        #ya con las cabeceras graficadas, lo siguiente es los nodos internos, o nodosCelda
        pivote = self.filas.primero
        posx = 0
        while pivote != None:
            pivote_celda : Nodo_Interno = pivote.acceso
            while pivote_celda != None:
                # --- buscamos posy
                pivotey = self.columnas.primero
                posy_celda = 0
                while pivotey != None:
                    if pivotey.id == pivote_celda.coordenadaY: break
                    posy_celda += 1
                    pivotey = pivotey.siguiente
                if pivote_celda.caracter == '*':
                    contenido += '\n\tnode[label="*" fillcolor="black" pos="{},-{}!" shape=box]i{}_{};'.format( #pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    )
                elif pivote_celda.caracter == 'E':
                    contenido += '\n\tnode[label="E" fillcolor="green" pos="{},-{}!" shape=box]i{}_{};'.format( #pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    )
                elif pivote_celda.caracter == 'R':
                    contenido += '\n\tnode[label="R" fillcolor="gray" pos="{},-{}!" shape=box]i{}_{};'.format( #pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    )
                elif pivote_celda.caracter == 'C':
                    contenido += '\n\tnode[label="C" fillcolor="cyan" pos="{},-{}!" shape=box]i{}_{};'.format( #pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    )
                elif pivote_celda.caracter == 'M':
                    contenido += '\n\tnode[label="M" fillcolor="red" pos="{},-{}!" shape=box]i{}_{};'.format( #pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    )
                elif pivote_celda.caracter == 'W':
                    contenido += '\n\tnode[label=" " fillcolor="yellow" pos="{},-{}!" shape=box]i{}_{};'.format( #pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    )
                else:
                    contenido += '\n\tnode[label=" " fillcolor="white" pos="{},-{}!" shape=box]i{}_{};'.format( # pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    ) 
                pivote_celda = pivote_celda.derecha
            
            pivote_celda = pivote.acceso
            while pivote_celda != None:
                if pivote_celda.derecha != None:
                    contenido += '\n\ti{}_{}->i{}_{};'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY,
                    pivote_celda.derecha.coordenadaX, pivote_celda.derecha.coordenadaY)
                    contenido += '\n\ti{}_{}->i{}_{}[dir=back];'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY,
                    pivote_celda.derecha.coordenadaX, pivote_celda.derecha.coordenadaY)
                pivote_celda = pivote_celda.derecha
        
            contenido += '\n\tx{}->i{}_{};'.format(pivote.id, pivote.acceso.coordenadaX, pivote.acceso.coordenadaY)
            contenido += '\n\tx{}->i{}_{}[dir=back];'.format(pivote.id, pivote.acceso.coordenadaX, pivote.acceso.coordenadaY)
            pivote = pivote.siguiente
            posx += 1
        
        pivote = self.columnas.primero
        while pivote != None:
            pivote_celda : Nodo_Interno = pivote.acceso
            while pivote_celda != None:
                if pivote_celda.abajo != None:
                    contenido += '\n\ti{}_{}->i{}_{};'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY,
                    pivote_celda.abajo.coordenadaX, pivote_celda.abajo.coordenadaY)
                    contenido += '\n\ti{}_{}->i{}_{}[dir=back];'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY,
                    pivote_celda.abajo.coordenadaX, pivote_celda.abajo.coordenadaY) 
                pivote_celda = pivote_celda.abajo
            contenido += '\n\ty{}->i{}_{};'.format(pivote.id, pivote.acceso.coordenadaX, pivote.acceso.coordenadaY)
            contenido += '\n\ty{}->i{}_{}[dir=back];'.format(pivote.id, pivote.acceso.coordenadaX, pivote.acceso.coordenadaY)
            pivote = pivote.siguiente
                
        contenido += '\n}'
        #--- se genera DOT y se procede a ecjetuar el comando
        dot = "matriz_{}_dot.txt".format(nombre)
        with open(dot, 'w') as grafo:
            grafo.write(contenido)
        result = "matriz_{}.pdf".format(nombre)
        os.system("neato -Tpdf " + dot + " -o " + result)