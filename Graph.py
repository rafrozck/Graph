from Vertex import Vertex
from Edge import Edge


class Graph:
    # Initialize directed or undirected graph
    def __init__(self, type='undirected'):
        self.Vertices = []
        self.Edges = []
        self.type = type

    # Function adds vertex to graph
    def add_vertex(self, v):
        if isinstance(v, Vertex) and v.name not in self.Vertices:
            self.Vertices.append(v)
            return True
        else:
            return False

    def delete_vertex(self, name):
        if self.is_in_graph(name):
            vertex = self.return_vertex(name)
            self.Vertices.remove(vertex)
            return True
        else:
            return False

    # Function adds edge between two vertices with specified weight
    def add_edge(self, v1, v2, weight):
        if isinstance(v1, Vertex) and isinstance(v2, Vertex) and weight > 0:
            if type == 'undirected':
                e = Edge(weight)
            else:
                e = Edge(weight, True)

            e.connect_vertices(v1, v2)
            self.Edges.append(e)

            return True
        else:
            return False

    # Function indicates if vertex with specified name exists in graph
    def is_in_graph(self, name):
        for v in self.Vertices:
            if name == v.name:
                return True

        return False

    # Function returns vertex with specified name
    def return_vertex(self, name):
        for v in self.Vertices:
            if name == v.name:
                return v

    # Function returns weight of edge connecting two vertices
    # Function returns None if vertices are not neighbours or at least one of them does not exist
    def find_edge(self, v1_name, v2_name):
        if self.is_in_graph(v1_name) and self.is_in_graph(v2_name):
            v1, v2 = self.return_vertex(v1_name), self.return_vertex(v2_name)
            if v2 in v1.adj_list:
                for e in self.Edges:
                    if (v1.name == e.v1 and v2.name == e.v2) or (v1.name == e.v2 and v2.name == e.v1):
                        return e.weight
            else:
                print('Vertices: ' + v1_name + ' and ' + v2_name + ' are not neighbours')
                return None
        else:
            print('Pair of vertices does not exist')
            return None

    # Function prints vertives in graph and their neighbours
    def print_vertices(self):
        print('Vertex list: ')
        for i in range(len(self.Vertices)):
            print(str(i + 1) + '.\t' + self.Vertices[i].name + ' || Neighbours: ' +
                  str(self.Vertices[i].print_neighbours()))

    # Function prints edges in graph with weight and two connected vertices names
    def print_edges(self):
        if self.type == 'undirected':
            connect_sign = '--'
        else:
            connect_sign = '->'

        print('Edges list: ')
        for i in range(len(self.Edges)):
            print(str(i + 1) + '.\t' + 'Edge with weight = ' + str(self.Edges[i].weight) + ' || Connected: ' +
                  connect_sign + ' ' + str(self.Edges[i].print_joints()))
