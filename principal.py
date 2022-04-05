from xml.dom import minidom
from Lectura import Rs, CI 
from Lectura import Lectura as Lc
from MatrizDispersa import MatrizDispersa
import sys, os, time


def load_animation(that,esto):
        load_str = that+esto
        ls_len = len(load_str)  
        animation = "|/-\\"
        anicount = 0
        counttime = 0        
        i = 0                     
        while (counttime != 200): 
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




Lc.lecture('entrada.xml')

menu = """
1. Mostrar Ciudades
2. Mostrar Robots
3. Misión
4. Salir"""

opcion=0
while(opcion != 4):
    print(menu)
    opcion = input("Ingrese una opción: \n")
    if(opcion == "1"):
        CI.mostrar()
        CI.mostrar2()
    elif(opcion == "2"):
        Rs.mostrar()
        Rs.mostrar2()
    elif(opcion == "3"):
        print("Misiónes disponibles:")
        CI.enliztar()
        CI.mostrar2()
        ciudad = input("Seleccione el numero de ciudad para ver sus misiones: \n")
        ciudadSelect = CI.buscarNodo(ciudad)
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
        load_animation('comenzando mision: ',mision.mor().lower())
        load_animation('mision completada: ','cargando datos')
        print(mision.nodoMis.getCaracter())
        if(str(mision.nodoMis.getCaracter())=='C'):
            ciudadSelect.casillas.buscarCaminoRescate(entrada.nodoMis,mision.nodoMis)
            ciudadSelect.casillas.graficarRecorrido('Mision_Completada')
            ciudadSelect.casillas.quitarW()
        else:
            print('nel')

    elif(opcion == "4"):
        print("Adios")
        break



  








'''aux = CI.cabecera
while aux != None:
    aux.casillas.graficarDibujo(aux.nombre)
    aux = aux.siguiente'''
