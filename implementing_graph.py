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

    def addVertex(self,key):
        newVertex = vertex(key)
        self.numVertices +=1
        self.VertList[key] = newVertex
        return newVertex

    def addEdge(self,f,t,weight):
        if f not in self.VertList:
            newVertex = VertList(f)
        if t not in self.VertList:
            newVertex = VertList(t)
        self.VertList[f].addNeighbour(self.VertList[t],weight)

    def getVertex(self,key):
        return self.VertList[key]

    def getVertices(self):
        return self.VertList.keys()


my_graph = Graph()
my_graph.addVertex("A")
print my_graph.getVertices()
my_graph.addVertex("B")
print my_graph.getVertices()
my_graph.addEdge("A","B",10)
print my_graph.getVertex("A").getConnections()
