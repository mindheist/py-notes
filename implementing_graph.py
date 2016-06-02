# Couple of Classes in this implementation of Graph Datastructure

class vertex:
    def __init__(self,key):
        self.key = key
        self.connectedTo = {} # note this is a weighted Graph, we are saving the node and weight

    def getId(self):
        return self.key

    def addNeighbour(self,nbr,weight):
        self.connectedTo[nbr] = weight

    def getConnections(self):
        return self.connectedTo.keys()

    def getWeight(self,node):
        if node in connectedTo.keys():
            return self.connectedTo[node]
        else:
            return -1

class Graph:
    def __init__(self):
        self.numVertices = 0
        self.VertList = {}
