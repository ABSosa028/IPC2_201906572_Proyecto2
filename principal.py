from xml.dom import minidom
from Lectura import Rs, CI 
from Lectura import Lectura as Lc
from MatrizDispersa import MatrizDispersa
import sys, os, time
import webbrowser
from tkinter import *
from tkinter import filedialog as fd





def load_animation(that,esto):
        load_str = that+esto
        ls_len = len(load_str)  
        animation = "|/-\\"
        anicount = 0
        counttime = 0        
        i = 0                     
        while (counttime != 75): 
            time.sleep(0.075)  
            load_str_list = list(load_str)  
            x = ord(load_str_list[i]) 
            y = 0                             
            if x != 32 and x != 46:              
                if x>90: 
                    y = x-32
                else: 
                    y = x + 32
                load_str_list[i]= chr(y) 
            res =''              
            for j in range(ls_len): 
                res = res + load_str_list[j] 
            sys.stdout.write("\r"+res + animation[anicount]) 
            sys.stdout.flush() 
            load_str = res 
            anicount = (anicount + 1)% 4
            i =(i + 1)% ls_len 
            counttime = counttime + 1
        if os.name =="nt": 
            os.system("cls") 
        else: 
            os.system("clear") 



menu = """
c. Cargar Archivo
1. Mostrar Ciudades
2. Mostrar Robots
3. Misión
4. Salir"""

opcion=0
while(opcion != 4):
    print(menu)
    opcion = input("Ingrese una opción: \n")
    if(opcion == "c" or opcion == "C"):
        print('seleccione un archivo de entrada')
        filename = fd.askopenfilename()
        print(filename)
        Lc.lecture(filename)
    elif(opcion == "1"):
        if(CI.cabecera == None):
            print("\nNo hay ciudades cargadas")
            input('presione enter para continuar')
            continue
        CI.mostrar()
        CI.mostrar2()
    elif(opcion == "2"):
        if(CI.cabecera == None):
            print("\nNo hay ciudades cargadas")
            input('presione enter para continuar')
            continue
        Rs.mostrar()
        Rs.mostrar2()
    elif(opcion == "3"):
        if(CI.cabecera == None):
            print("\nNo hay ciudades cargadas")
            input('presione enter para continuar')
            continue
        print("\n \nMisiónes disponibles:")
        CI.enliztar()
        CI.mostrar2()
        ciudad = input("Seleccione el numero de ciudad para ver sus misiones: \n")
        ciudadSelect = CI.buscarNodo(ciudad)
        ciudadSelect.mostrar()
        print('------------------------------------------------------')
        print('Ciudad seleccionada:\n\t'+str(ciudadSelect.getnombre()))
        print('------------------------------------------------------')
        misiones = ciudadSelect.casillas.MostrarMisiones()
        misiones.mostrar()
        mselect = input("Seleccione una mision: \n")
        mision = misiones.buscarNodo(int(mselect))
        print('------------------------------------------------------------------')
        print('Mision seleccionada:\n\t'+str(ciudadSelect.getnombre()))
        mision.mostrar()
        print('------------------------------------------------------------------')
        print("\n")
        print('------------------------------------------------------------------')
        print("Robots disponibles para esta mision:")
        tipoMis = mision.gettipo()
        Rs.enliztar(tipoMis)
        if(tipoMis == "R"):
            Rs.mostrartp('ChapinFighter')
        elif(tipoMis == "C"):
            Rs.mostrartp('ChapinRescue')
        print('------------------------------------------------------------------')
        opR = input("Seleccione un robot por su id: \n")
        robot = Rs.buscarNodo(opR)
        if(robot != None):
            print('------------------------------------------------------------------')
            print('Robot seleccionado:\n\t'+str(robot.getNombre()))
            print('------------------------------------------------------------------')
        print('\n')
        print('\n')
        print('Entradas disponibles:')
        entradas = ciudadSelect.casillas.MostrarEntradas()
        entradas.mostrarE()
        print('------------------------------------------------------------------')
        entradaS = input("Seleccione una Entrada: \n")
        entrada = entradas.buscarNodo(int(entradaS))
        print('------------------------------------------------------------------')
        print('\n')
        print('------------------------------------------------------------------')
        print('Entrada seleccionada:\n\t'+str(ciudadSelect.getnombre()))
        print(entrada.mor())
        print('------------------------------------------------------------------')
        print("\n")
        #load_animation('comenzando mision: ',mision.mor().lower())
        if(str(mision.nodoMis.getCaracter())=='C'):
            intent = (ciudadSelect.casillas.buscarCaminoRescate(entrada.nodoMis,mision.nodoMis))
            if(intent==True):
                ciudadSelect.casillas.graficarRecorrido('Mision_Completada')
            ciudadSelect.casillas.quitarW()
        elif(str(mision.nodoMis.getCaracter())=='R'):
            ciudadSelect.militares.mostrar()
            intent =(ciudadSelect.casillas.buscarCaminoRecurso(entrada.nodoMis,mision.nodoMis,robot,ciudadSelect.militares))
            if(intent==True):
                ciudadSelect.casillas.graficarRecorrido('Mision_Completada')
                webbrowser.open('matriz_Recursos.pdf'.format(ciudadSelect.getnombre()))
            ciudadSelect.casillas.quitarW()


    elif(opcion == "4"):
        print("Adios")
        break




'''aux = CI.cabecera
while aux != None:
    aux.casillas.graficarDibujo(aux.nombre)
    aux = aux.siguiente'''
