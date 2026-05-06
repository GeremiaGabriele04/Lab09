import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._nodes = []
        self._idMapAeroporto = {}
        self._nodo = DAO.getAllNodes()
        for a in self._nodo:
            self._idMapAeroporto[a.ID] = a
        self._graph = nx.Graph()

    def buildGraph(self, x):
        self._graph.clear()
        #aggiungo gli archi secondo il vincolo di x
        self.addEdgesPesatiV2(x)
        #aggiungo i nodi
        #self._graph.add_nodes_from(self._nodes)

    def addEdgesPesatiV2(self, x):
        # delega il calcolo del peso alla query nel DAO, semplifica la vita
        allEdgesWPeso = DAO.getAllEdgesPesati()

        for e in allEdgesWPeso:
            peso = 0
            volte = 0
            peso += e[2]
            volte += e[3]

            if self.presenteIn(e[1], e[0], allEdgesWPeso) is not None:
                tupla = self.presenteIn(e[1], e[0], allEdgesWPeso)
                peso += tupla[2]
                volte += tupla[3]

            media = peso / volte

            if media > x:
                u = self._idMapAeroporto[e[0]]
                v = self._idMapAeroporto[e[1]]
                self._graph.add_edge(u, v, weight=media)


    def presenteIn(self, i1, i0, lista):
        for i in lista:
            if i1 == i[0]:
                if i0 == i[1]:
                    return i
        return None

    def get_numnodi(self):
        return len(self._graph.nodes)

    def get_numarchi(self):
        return len(self._graph.edges)