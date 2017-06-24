import matplotlib.pyplot as renderer

from core.Graph import Graph

class Renderer():

    def __init__(self, outputPath, nodeSize=700, edgeWidth=6):
        self.graph = Graph(nodeSize, edgeWidth)
        self.outputPath = outputPath

    def render(self):
        self.graph.render()
        renderer.axis('off')
        renderer.savefig(self.outputPath)
        renderer.show()
