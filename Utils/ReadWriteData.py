from .Graph import Graph

def read_data(filename: str):
    graph = Graph()
    with open(filename, 'r') as file:
        strings = file.readlines()

        n, m = tuple(int(x) for x in strings[0].split())
        users = tuple(int(x) for x in strings[1].split())

        for string in strings[2:]:
            first, last, weight = tuple(int(x) for x in string.split())
            graph.create_edges_from_vertexes(first, last, weight)

    return n, m, users, graph

def write_data(filename, data):
    data = str(data)
    with open(filename, 'w') as file:
        file.write(data)