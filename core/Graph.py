import networkx

class Graph():

    def __init__(self, nodeSize=700, edgeWidth=6):
        self.graph = networkx.Graph()
        self.nodeSize = nodeSize
        self.edgeWidth = edgeWidth

    def getPosition(self):
        return networkx.spring_layout(self.graph)

    def render(self):
        position = self.getPosition()
        self.renderNodes(position)
        self.renderEdges(position)

    def renderNodes(self, position):
        networkx.draw_networkx_nodes(self.graph, position, node_size=self.nodeSize)

    def renderEdges(self, position):
        networkx.draw_networkx_edges(self.graph, position,
                                     edgelist=self.graph.edges(data=True),
                                     width=self.edgeWidth)
