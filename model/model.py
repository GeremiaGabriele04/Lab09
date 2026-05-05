import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._nodes = []
        self._idMapAeroporto = {}
        self._graph = nx.Graph()


    def buildGraph(self):
        #aggiungo i nodi
        self._graph.add_nodes_from(self._nodes)

    def addEdgesPesatiV2(self, x):
        # delega il calcolo del peso alla query nel DAO, semplifica la vita
        self._graph.clear()
        allEdgesWPeso = DAO.getAllEdgesPesati()
        # (id_stazP, id_stazA, peso)

        for e in allEdgesWPeso:
            distanza = e[2]/e[3]
            if  distanza > x:
                self._nodes = DAO.getAllNodes(e[0], e[1])
                self.buildGraph()
                for a in self._nodes:
                    self._idMapAeroporto[a.ID] = a
                u = self._idMapAeroporto[e[0]]
                v = self._idMapAeroporto[e[1]]
                self._graph.add_edge(u, v, weight=distanza)

    def get_numnodi(self):
        return len(self._graph.nodes())

    def get_numarchi(self):
        return len(self._graph.edges())