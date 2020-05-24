from Vertex import Vertex
from Graph import Graph

v = [Vertex('A'), Vertex('B'), Vertex('C')]

G = Graph()
G.add_vertex(v[0])
G.add_vertex(v[1])
G.add_vertex(v[2])

G.add_edge(v[0], v[1], 32)
G.add_edge(v[0], v[2], 11)

G.print_vertices()
G.print_edges()

