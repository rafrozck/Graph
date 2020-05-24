from Vertex import Vertex
from Edge import Edge

class Graph:
    Vertices = []
    Edges = []

    def add_vertex(self, v):
        if isinstance(v, Vertex) and v.name not in self.Vertices:
            self.Vertices.append(v)
            return True
        else:
            return False

    def add_edge(self, v1, v2, weight):
        if isinstance(v1, Vertex) and isinstance(v2, Vertex) and weight > 0:
            e = Edge(weight)
            e.connect_vertices(v1, v2)
            self.Edges.append(e)
            return True
        else:
            return False

    def print_vertices(self):
        print('Vertex list: ')
        for i in range(len(self.Vertices)):
            print(self.Vertices[i].name + ' || Neighbours: ' + str(self.Vertices[i].print_neighbours()))

    def print_edges(self):
        print('Edges list: ')
        for i in range(len(self.Edges)):
            print('Edge with weight = ' + str(self.Edges[i].weight) + ' || Connected: ' + str(self.Edges[i].print_joints()))



