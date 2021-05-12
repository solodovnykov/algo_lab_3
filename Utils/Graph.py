class Graph:

    def __init__(self):
        self.connections = {}

    def create_edges_from_vertexes(self, first_vertex_id, second_vertex_id, weight):

        if weight < 0:
            raise ValueError('Weights must be > 0')
        if (type(first_vertex_id) is not int) | (type(second_vertex_id) is not int) | (type(weight) is not int):
            raise TypeError('Only integer values')

        self.create_edge(first_vertex_id, second_vertex_id, weight)

        self.create_edge(second_vertex_id, first_vertex_id, weight)


    def create_edge(self, vertex_from: int, vertex_to: int, edge_weight: int):
        if vertex_from in self.connections.keys():
            if (vertex_to, edge_weight) not in self.connections[vertex_from]:
                self.connections[vertex_from].append((vertex_to, edge_weight))
        else:
            self.connections[vertex_from] = [(vertex_to, edge_weight)]

    def print_graph(self):
        for element in self.connections:
            print(element, self.connections[element])
