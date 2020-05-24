from Vertex import Vertex

class Edge:
    def __init__(self, weight):
        self.weight = weight
        self.v1 = None
        self.v2 = None

    def connect_vertices(self, v1, v2):
        if isinstance(v1, Vertex) and isinstance(v2, Vertex):
            v1.add_neigbour(v2)
            v2.add_neigbour(v1)
            self.v1 = v1.name
            self.v2 = v2.name
            return True
        else:
            return False

    def print_joints(self):
        return (self.v1, self.v2)
