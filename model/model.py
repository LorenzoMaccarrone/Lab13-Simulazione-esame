from database.DAO import DAO
import networkx as nx
import copy
class Model:
    def __init__(self):
        self._allStates = DAO.getAllStates()
        self._idMap = {}
        for a in self._allStates:
            self._idMap[a.id] = a
    def getYear(self):
        return DAO.getAllYear()
    def getShape(self):
        return DAO.getAllShape()
    def creaGrafo(self, year, shape):
        self._grafo = nx.Graph()
        self._grafo.add_nodes_from(self._allStates)
        self.addEdges(year, shape)
    def addEdges(self, anno, forma):
        for a in self._allStates:
            if a.Neighbors is not None:
                splittedList = a.Neighbors.split()
                #ho i vicini dello stato considerato, aggiungo gli archi
                for i in splittedList:
                    peso = 0
                    peso=self.calcolaPeso(anno, forma, a, self._idMap[i])
                    self._grafo.add_edge(a,self._idMap[i],weight=peso)
    def calcolaPeso(self, anno, forma,v0,v1):
        #anno è un intero mentre forma una stringa v0 e v1 sono oggetti di tipo state
        listaPeso=DAO.calcolaPeso(anno, forma, v0.id, v1.id)
        if len(listaPeso)!=0:
            return int(listaPeso[0])
        else:
            return 0
        #il dao mi ritorna come risultato una lista di pesi, se la lista è vuota vuol dire che tra quei
        #due stati non ci sono stati avvistamenti, altrimenti ritorno l'elemento in posizione
        #0 della lista, ovvero il peso effettivo

    def pesiArchiAdiacenti(self):
        printPesi= list() #sarà una lista di tuple
        for a in self._allStates:
            peso=0
            listaPesi= list()
            #da calcolare il peso prendendo il peso dei vicini
            for i in self._grafo.neighbors(a):
                listaPesi=list(self._grafo.get_edge_data(a,i))
            for b in listaPesi:
                peso+=int(b)
            pesoVicini= a, peso
            printPesi.append(copy.deepcopy(pesoVicini))#se no copio la stessa tupla su tutti le entry della lista
        return printPesi

    def getNumNodi(self):
        return len(self._grafo.nodes)

    def getNumArchi(self):
        return len(self._grafo.edges)








