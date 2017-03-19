class Node(object):
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def __str__(self):
        return self.name

class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def getSource(self):
        return self.src

    def getDestination(self):
        return self.dest

    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName()

class WeightedEdge(Edge):
    def __init__(self, src, dest, weight):
        Edge.__init__(self,src, dest)
        #super().__init__(src, dest) also works
        self.weight = weight
        
    def getWeight(self):
        return self.weight
        
    def __str__(self):
        t = super().__str__() + ' (%d)'%(self.weight)
        return t

    
class Digraph(object):

    def __init__(self):
        self.edges = {}

    def addNode(self, node):
        if node in self.edges:
            raise ValueError('Duplicate Node')
        else:
            self.edges[node] = []

    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self.edges and dest in self.edges):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)

    def childrenOf(self,node):
        return self.edges[node]

    def hasNode(self, node):
        return node in self.edges

    def getNode(self, name):
        for n in self.edges:
            if n.getName() == name:
                return n
        raise NameError(name)

    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result += src.getName() + '->' + dest.getName() + '\n'
        return result[:-1]

class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)

def printPath(path):
    """Assumes path is a list of nodes"""
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + '->'
    return result 

def DFS(graph, start, end, path, shortest, toPrint = False):
    path = path + [start]
    if toPrint:
        print('Current DFS path:', printPath(path))
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path:
            if shortest == None or len(path) < len(shortest):
                newPath = DFS(graph, node, end, path, shortest, toPrint)
                if newPath != None:
                    shortest = newPath
            elif toPrint:
                print('Already visited', node)
    return shortest

def shortestPath(graph, start, end):
    return BFS(graph, start, end, True)

def BFS(graph, start, end, toPrint = False):
    initPath = [start]
    pathQueue = [initPath]
    if toPrint:
        print('Current BFS path:', printPath(pathQueue))
    while len(pathQueue) != 0:
        tmpPath = pathQueue.pop(0)
        print('Current BFS path:', printPath(tmpPath))
        lastNode = tmpPath[-1]
        if lastNode == end:
            return tmpPath
        for nextNode in graph.childrenOf(lastNode):
            if nextNode not in tmpPath:
                newPath = tmpPath +[nextNode]
                pathQueue.append(newPath)
    return None

def buildCityGraph(graphType):
    g = graphType()
    for name in ('Boston', 'Providence', 'New York', 'Chicago',
                 'Denver', 'Phoenix', 'Los Angeles'): #Create 7 nodes
        g.addNode(Node(name))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('Providence')))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('Boston')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('New York'), g.getNode('Chicago')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Denver')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Los Angeles'), g.getNode('Boston')))
    return g

def buildLine(graphType):
    g = graphType()
    nodes = []
    nodes.append(Node('ABC'))
    nodes.append(Node('ACB'))
    nodes.append(Node('BAC'))
    nodes.append(Node('BCA'))
    nodes.append(Node('CAB'))
    nodes.append(Node('CBA'))
    for n in nodes: g.addNode(n)
    g.addEdge(Edge(g.getNode('ABC'), g.getNode('BAC')))
    g.addEdge(Edge(g.getNode('ABC'), g.getNode('ACB')))
    g.addEdge(Edge(g.getNode('ACB'), g.getNode('CAB')))
    g.addEdge(Edge(g.getNode('BAC'), g.getNode('BCA')))
    g.addEdge(Edge(g.getNode('BCA'), g.getNode('CBA')))
    g.addEdge(Edge(g.getNode('CAB'), g.getNode('CBA')))
    
    return g
##
##g = buildCityGraph(Digraph)
##sp = shortestPath(g, g.getNode('Boston'), g.getNode('Phoenix'))
##for i in sp:
##    print(i)

g = buildLine(Graph)
print(g)


