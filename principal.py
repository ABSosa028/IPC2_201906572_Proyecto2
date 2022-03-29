from xml.dom import minidom
from Lectura import Rs, CI 
from Lectura import Lectura as Lc
from MatrizDispersa import MatrizDispersa

Lc.lecture('entrada.xml')

menu = """
1. Mostrar Ciudades
2. Mostrar Robots
3. Misión
4. Salir"""


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
    
elif(opcion == "4"):
    print("Adios")











'''aux = CI.cabecera
while aux != None:
    aux.casillas.graficarDibujo(aux.nombre)
    aux = aux.siguiente'''
