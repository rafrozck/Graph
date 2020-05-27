from Vertex import Vertex
from Graph import Graph

v = [Vertex('A'), Vertex('B'), Vertex('C'), Vertex('D'), Vertex('E')]
G = Graph('undirected')

for i in v:
    G.add_vertex(i)

G.add_edge(v[0], v[1], 6)
G.add_edge(v[0], v[3], 1)
G.add_edge(v[1], v[3], 2)
G.add_edge(v[1], v[4], 2)
G.add_edge(v[3], v[4], 1)
G.add_edge(v[1], v[2], 5)
G.add_edge(v[4], v[2], 5)

G.print_vertices()
G.print_edges()






