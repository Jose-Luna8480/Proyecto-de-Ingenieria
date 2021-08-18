import csv
from time import time
import json
import sys

############################ALGORITMO DE DIJKSTRA############################
class Nodo:
    # esta clase define los nodos de las graficas.
    # constructor
    def __init__(self, i):
        self.name = i  # nombre del nodo
        self.vecinos = []  # vecinos del nodo
        self.visitado = False  # Estado de visita
        self.padre = None  # El padre de ese nodo
        self.costo = float('inf')  # El costo que al principio es infinito

    def agregarVecino(self, v, c):  # v es el Id del vecino y c es el costo de la arista entre los vecinos
        if not v in self.vecinos:  # En dado caso que el vecino no este ya en la lista, se agrega.
            self.vecinos.append([v, c])  # agregar nombre del nodo vecino y el costo


class Grafica:
    # constructor
    def __init__(self):
        self.vertices = {}  # Declarar los vertices en un diccionario

    def agregarVertice(self, name):
        if not name in self.vertices:
            self.vertices[name] = Nodo(name)  # Se agrega un Nodo a la grafica
            print("Agregado a Dijkstra Beacon con ID {}".format(name))

    def agregarArista(self, a, b, c):
        if a in self.vertices and b in self.vertices:
            self.vertices[a].agregarVecino(b, c)  # Se declara una union de nodos y su costo
            self.vertices[b].agregarVecino(a, c)  # Se hace bidireccional para no tener problemas
            print(
                "La unión entre {} y {} se realizó de manera bidireccional sin errores con un costo de {}".format(a, b,
                                                                                                                  c))
        else:
            print("Uno de los nodos ({}, {}) no ha sido declarado. Omitiendo arista.".format(a, b))

    def minimo(self, lista_noVisitados):
        if len(lista_noVisitados) > 0:
            m = self.vertices[lista_noVisitados[0]].costo
            v = lista_noVisitados[0]
            for item in lista_noVisitados:
                if m > self.vertices[item].costo:
                    m = self.vertices[item].costo
                    v = item
            return v

    def camino(self, b):
        # Método que va guardando en la lista llamada 'camino' los nodos en el orden que sean visitados y actualizando dicha
        # lista con los vértices con el menor cost
        camino = []
        nodoActual = b
        while nodoActual != None:
            camino.insert(0, nodoActual)
            nodoActual = self.vertices[nodoActual].padre
            """
            try:
                nodoActual = self.vertices[nodoActual].padre
            except:
                print("El beacon con ID:{} no está definido en la topología, por lo que no se puede elaborar la ruta al punto solicitado".format(nodoActual))

                return False
            """
        return [camino, self.vertices[b].costo]

    def Dijkstra(self, a):  # Desde aqui se correra el algoritmo
        if a in self.vertices:
            self.vertices[a].costo = 0  # Le agregamos un costo de 0 al nodo inicial
            nodoActual = a  # Definimos el nodo actual
            noVisitados = []  # Se crea la lista de nodos no visitados para ir agarrandolos poco a poco
            for v in self.vertices:
                if v != a:
                    self.vertices[v].costo = float('inf')  # Resto de los nodos inica con costo infinito
                self.vertices[v].padre = None  # Todos los nodos inician sin un padre
                noVisitados.append(v)  # Agregamos todos los nodos a la lista de noVisitados

            while len(noVisitados) > 0:
                for vecino in self.vertices[nodoActual].vecinos:  # Recorremos a los vecinos del nodo Actual
                    if not self.vertices[vecino[0]].visitado:  # Aseguramos que no este visitado
                        if self.vertices[nodoActual].costo + vecino[1] < self.vertices[vecino[
                            0]].costo:  # verificamos si el costo de llegar al nodo por esa via es menor al costo que ya tiene el nodo
                            self.vertices[vecino[0]].costo = self.vertices[nodoActual].costo + vecino[
                                1]  # si es menor, cambiamos el costo del nodo vecino
                            self.vertices[
                                vecino[0]].padre = nodoActual  # Asignamos como padre de ese vecino al nodo actual
                self.vertices[nodoActual].visitado = True
                noVisitados.remove(nodoActual)
                nodoActual = self.minimo(noVisitados)

        else:
            return False


############################ALGORITMO DE DIJKSTRA############################


class Beacon:
    def __init__(self, name, id, coordinates, users=0, neighbors={}, active=False, type='convencional', equivalent=''):
        self.name = name
        self.id = id
        self.coordinates = coordinates
        self.users = users
        self.neighbors = neighbors
        self.active = active
        self.type = type
        self.equivalent = equivalent


def getKey(dictionary, value):
    listItems = dictionary.items()
    for items in listItems:
        if items[1] == value:
            return items[0]
        else:
            pass


def determineCheapestPathDijkstra(dictionary, caminos):
    tempDict = {}
    for i in caminos:
        tempDict[i[1]] = i[0]  # Acomodados por peso: rutaDijkstra; tempDict = {20: ['A0', 'B0', 'C0', 'SAL0']}

    cheapestDijkstra = min(tempDict)

    tempDict2 = dict([(value, key) for key, value in dictionary.items()])  # Swap keys and values

    tempList = tempDict[cheapestDijkstra]
    for indx, item in enumerate(tempList):
        tempList[indx] = tempDict2[item]

    print("Ruta a seguir Dijkstra: ", tempList)  # tempList contiene la lista de beacons

    return cheapestDijkstra, tempList


def executeAlgorithm(g, salidas, beaconName, beaconsDesactivados, dictBeaconName_ID):
    for i in dictBeaconName_ID:
        dictBeaconName_ID[i] = dictBeaconName_ID[i][0]

    #print(dictBeaconName_ID)
    beaconID = dictBeaconName_ID[beaconName]

    caminos = []
    if beaconID in beaconsDesactivados or beaconID == None:
        print("El beacon de inicio está desactivado, por lo que no se puede proceder con el cálculo de la ruta.")
        sys.exit(1)
    else:
        g.Dijkstra(beaconID)
        for c in salidas:
            caminos.append(g.camino(dictBeaconName_ID[c]))

        value = determineCheapestPathDijkstra(dictBeaconName_ID, caminos)
        return value


def main():
    # Declaración de nodos y uniones para Dijkstra
    g = Grafica()
    dictBeaconName_ID = {}
    beacons = []
    enlacesExistentes = []
    escaleras = {}
    salidas = {}
    beaconsDesactivados = {}

    with open('data.txt') as json_file:
        data = json.load(json_file)  # leemos los datos que nos interesan del archivo JSON

    print("Estos son los datos: ", data)

    for p in data:  # Creamos la lista de beacons "beacons" y el diccionario "dictBeaconName_ID"
        for i in data[p]:
            new_Beacon = Beacon(p, i['id'], i['coordenadas'], i['usuarios'], i['vecinos'], i['activado'],
                                i['tipo'],
                                i['equivalente'])  # Creamos y guardamos objectos tipo Beacon en la lista "beacons"
            beacons.append(new_Beacon)
            dictBeaconName_ID[new_Beacon.name] = [new_Beacon.id, new_Beacon.coordinates]

    for beacon in beacons:  #Se agregan los vértices con los que trabajará el mapa de Dijkstra siempre y cuando no estén desactivados
        if (beacon.active):
            if beacon.type == 'escalera':
                escaleras[beacon.name] = (beacon.coordinates, beacon.equivalent)
            elif beacon.type == 'salida':
                salidas[beacon.name] = beacon.coordinates
            elif beacon.type == 'salidaPredeterminada':
                salidas[beacon.name] = beacon.coordinates
                salidaPredeterminada = True

            g.agregarVertice(beacon.id)

        else:
            beaconsDesactivados[beacon.id] = beacon.name

    for beacon in beacons:  # Se crean los enlaces con los que trabajará el mapa de Dijkstra
        for i in beacon.neighbors:
            x_columnas = pow(abs(beacon.coordinates[1] - dictBeaconName_ID[i[0]][1][1]), 2)
            y_filas = pow(abs(beacon.coordinates[0] - dictBeaconName_ID[i[0]][1][0]), 2)
            suma = x_columnas + y_filas
            distancia = pow(suma, 0.5)
            peso = ((beacon.users + i[2]) / 2) + distancia # Se determina el peso con el promedio de usuarios que hay en los extremos de cada enlace y la distancia entre ambos beacons

            ######DEBUG#####
            # print("Distancia calculada a partir de celdas de separación entre un beacon y otro: ", distancia)
            # print("Calculo de promedio basado en numero de usuarios en cada extremo del enlace: ",(beacon.users + i[2]) / 2))
            # print("Beacon actual: [{} {}], Beacon vecino: [{} {}], x: {}, y: {}, distancia: {}".format(beacon.name, beacon.coordinates, i[0], dictBeaconName_ID[i[0]][1], x_columnas, y_filas, distancia))

            if (str(beacon.id) + str(i[1]) in enlacesExistentes or str(i[1]) + str(beacon.id) in enlacesExistentes):
                pass
            else:
                g.agregarArista(beacon.id, i[1], peso)  # Crear enlaces no repetidos (1-2 es igual que 2-1)

            enlacesExistentes.append(str(beacon.id) + str(i[1]))
            enlacesExistentes.append(str(i[1]) + str(beacon.id))

    if salidaPredeterminada:

        beaconName = 'L2' #Aquí es donde se tiene que poner el nombre en String del beacon en donde empieza el usuario

        if not beaconName in dictBeaconName_ID:
            print("Beacon de partida no disponible o inexistente.")
            sys.exit(1)
        else:
            resultado = executeAlgorithm(g, salidas, beaconName, beaconsDesactivados, dictBeaconName_ID)
            rutaFinalBeacons = resultado[1] #Esta es la ruta en Beacons que debe ser traducida a latitud, longitud

    else:
        print(
            "Revise que todos los nodos tengan una ruta disponible a la salida designada como predeterminada y que esta última exista.")
        sys.exit(1)


if __name__ == '__main__':
    start_time = time()
    main()
    elapsed_time = time() - start_time
    print("Tiempo de ejecución de la rutina: %.10f seconds." % elapsed_time)





