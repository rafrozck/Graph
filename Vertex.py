class Vertex:
    def __init__(self, name):
        self.name = name
        self.adj_list = []

    def add_neigbour(self, vertex_neighbour):
        if vertex_neighbour not in self.adj_list:
            self.adj_list.append(vertex_neighbour)

    def delete_neighbour(self, vertex_neighbour):
        if vertex_neighbour in self.adj_list:
            self.adj_list.remove(vertex_neighbour)

    def print_neighbours(self):
        a = []
        for i in range(len(self.adj_list)):
            a.append(self.adj_list[i].name)
        return a
