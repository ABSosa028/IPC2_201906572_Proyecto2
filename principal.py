from xml.dom import minidom
from Lectura import Rs, Ml, CI 
from Lectura import Lectura as Lc
from MatrizDispersa import MatrizDispersa

Lc.lecture('entrada.xml')
aux = CI.cabecera
while aux != None:
    aux.casillas.graficarDibujo(aux.nombre)