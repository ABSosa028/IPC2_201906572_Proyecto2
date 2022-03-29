from xml.dom import minidom 
from AreaCiudad import AreaCiudad as ac

doc = minidom.parse("entrada.xml")
configuraciones = doc.getElementsByTagName("configuracion")
for c in configuraciones:
    ListaCiudades = c.getElementsByTagName("listaCiudades")
    for ciudad in ListaCiudades:
        Ciudades = ciudad.getElementsByTagName("ciudad")
        for Ciudad in Ciudades:
            n = Ciudad.getElementsByTagName("nombre")
            name = n[0].childNodes[0].data
            filas = str(n[0].getAttribute("filas"))
            columnas = str(n[0].getAttribute("columnas"))
            rows = Ciudad.getElementsByTagName("fila")
            unidadesMil = Ciudad.getElementsByTagName("unidadMilitar")
            Rows = ''                                                                                                                        
            for Fila in rows:
                Rows+=str(Fila.childNodes[0].data)
            
            for unidades in unidadesMil:
                f = unidades.getAttribute("fila")
                co = unidades.getAttribute("columna")
                v = unidades.childNodes[0].data
                x = 1
                y = 1
                valores = []
                for letra in Rows:
                    if(x>int(columnas)):
                        x  = 1
                        y += 1
                    x += 1 
                    if(f == y and x == co):
                        valores.append(int(v))
                    else:
                        valores.append(0)

            espacios = ac()
            espacios.CrearMatriz(columnas, filas, Rows,valores)

 

                
            #print(name+'  '+filas+'  '+columnas)
    ListaRobots = c.getElementsByTagName("robots")
    for robot in ListaRobots:
        Robot = robot.getElementsByTagName("robot")
        for Rob in Robot:
            nombree = Rob.getElementsByTagName("nombre")
            names = nombree[0].childNodes[0].data
            tipo = nombree[0].getAttribute("tipo")
            capacidad = nombree[0].getAttribute("capacidad")
            #print(names+"  "+capacidad+"   "+tipo)
