from Robot import Robot as Rb
from unidadMilitar import milicia as mg
from milicia import Milicia as Mg
from Ciudades import Ciudades as Cis
from Ciudad import Ciudad as Ci
from xml.dom import minidom 
from AreaCiudad import AreaCiudad as ac
from Robots import Robots as Rbs
from MatrizDispersa import MatrizDispersa



Rs = Rbs()
Ml = Mg()
CI = Cis()
class Lectura():
    def lecture(nme):
        doc = minidom.parse(nme)
        configuraciones = doc.getElementsByTagName("configuracion")
        for cuento in configuraciones:
            ListaCiudades = cuento.getElementsByTagName("listaCiudades")
            for ciudad in ListaCiudades:
                Ciudades = ciudad.getElementsByTagName("ciudad")
                for Ciudad in Ciudades:
                    n = Ciudad.getElementsByTagName("nombre")
                    name = n[0].childNodes[0].data
                    filas = str(n[0].getAttribute("filas"))
                    columnas = str(n[0].getAttribute("columnas"))
                    rows = Ciudad.getElementsByTagName("fila")
                    unidadesMil = Ciudad.getElementsByTagName("unidadMilitar")
                    arch = open('{}.txt'.format(name), 'w')
                    for unidades in unidadesMil:
                        f = unidades.getAttribute("fila")
                        co = unidades.getAttribute("columna")
                        v = unidades.childNodes[0].data
                        newMil = mg(co,f,v)
                        Ml.insert(newMil) 
                    coun = 0                                                                                                                    
                    for Fila in rows:
                        coun+=1
                        Res=str(Fila.childNodes[0].data)
                        Res=Res.replace("\"", "")
                        for unidades in unidadesMil:
                            fc = unidades.getAttribute("fila")
                            coc = unidades.getAttribute("columna")
                            if(int(fc)==coun):
                                lista = list(Res)
                                lista[int(coc)-1] = 'M'
                                Res = ''.join(lista)
                        arch.write(Res)
                        arch.write('\n')
                    arch.close()
                    
                        
                    matriz =MatrizDispersa(0)
                    with open('{}.txt'.format(name)) as archivo:
                        l=0
                        c=0
                        lineas=archivo.readlines()
                        for linea in lineas:
                            columnas=linea
                            l+=1
                            for col in columnas:
                                if col != '\n':
                                    c+=1
                                    matriz.insert(l,c,col)
                            c=0
                            matriz.graficarDibujo('ciudadGotica')
                    
                    newCiudad = Ci(name,filas,columnas,matriz, Ml)
                    CI.insertar(newCiudad)
        

                        
            ListaRobots = cuento.getElementsByTagName("robots")
            for robot in ListaRobots:
                Robot = robot.getElementsByTagName("robot")
                cod = 1
                for Rob in Robot:
                    nombree = Rob.getElementsByTagName("nombre")
                    names = nombree[0].childNodes[0].data
                    tipo = nombree[0].getAttribute("tipo")
                    capacidad = nombree[0].getAttribute("capacidad")
                    Rn = Rb(cod, names, tipo, capacidad, 1)
                    Rs.insert(Rn)
                    #print(names+"  "+capacidad+"   "+tipo)
                    cod += 1
