import copy

from database.DAO import DAO
import networkx as nx



class Model:
    def __init__(self):
        self.sumDuration = None
        self.incrementalPath = None
        self.DAO = DAO()
        self.graph = None
        self.listNodes = None
        self.idMapFilm = {}



    def createGraph(self, rank):
        listNodes = self.DAO.getNodes()
        listEdges = self.DAO.getEdges(rank)
        self.graph = nx.Graph()
        for node in listNodes:
            self.idMapFilm[node.id] = node
        self.graph.add_nodes_from(listNodes)
        for edge in listEdges:
            self.graph.add_edge(self.idMapFilm[int(edge[0])], self.idMapFilm[int(edge[1])], weight=int(edge[2]))

    def getHighFilmGrade(self):
        HighFilmGradeNode = None
        HighFilmGradeSumWeight = 0
        for node in self.graph:
            sumWeight = 0
            for neighbor in self.graph.neighbors(node):
                sumWeight += self.graph[node][neighbor]["weight"]
            if sumWeight > HighFilmGradeSumWeight:
                HighFilmGradeSumWeight = sumWeight
                HighFilmGradeNode = node
        return HighFilmGradeNode, HighFilmGradeSumWeight




    def getIncrementalPath(self, source):
        self.incrementalPath = []
        partial = [source]
        print("Inizio ricorsione")
        self.recursion(
            source= source,
            partial= partial,
            predWeight = 0
        )
        print(self.incrementalPath)
        print("\nFINE\n")

        return self.incrementalPath

    def recursion(self, source, partial, predWeight):

        if len(partial) > len(self.incrementalPath):
            print("\n---------------------------------")
            print("aggiornamento self.incrementalPath")
            print(partial)
            self.incrementalPath = copy.deepcopy(partial)

        for neighbor in self.graph.neighbors(source):
            actualWeight = self.graph[source][neighbor]["weight"]
            if neighbor not in partial and actualWeight >= predWeight:
                print("node valido")
                partial.append(neighbor)
                self.recursion(neighbor, partial, actualWeight)
                print("NUOVA RICORSIONE")
                partial.pop()
            else:
                print("nodo non valido")
                return






