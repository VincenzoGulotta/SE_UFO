import networkx as nx
from database.dao import DAO
from geopy import distance

class Model:
    def __init__(self):
        self.G = nx.Graph()
        self.dict_anni_forme = None
        self.coppie_pesate = []
        self.stati = None
        self.pesi_totali = {}
        self.percorso = []
        self.distanza = 0


    def get_anni_forme(self):
        self.dict_anni_forme = DAO.get_anni_forme()

    def crea_grafo(self, year, shape):
        coppie = DAO.get_coppie()
        for coppia in coppie:
            peso = DAO.get_coppie_peso(year, shape, coppia[0].id, coppia[1].id)
            #print(year, shape, coppia[0].id, coppia[1].id, peso)
            if peso is not None:
                self.G.add_edge(coppia[0], coppia[1], weight = peso)
            else:
                self.G.add_edge(coppia[0], coppia[1], weight = 0)

        self.stati = DAO.get_stati()
        for item in self.stati:
            stato = self.stati[item]
            self.G.add_node(stato)

        nodi = self.G.number_of_nodes()
        archi = self.G.number_of_edges()

        for node1 in self.G.nodes():
            weight = 0
            for node2 in self.G.neighbors(node1):
                weight += self.G[node1][node2]['weight']
            self.pesi_totali[node1] = weight

        return (nodi, archi)












