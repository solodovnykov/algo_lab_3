from Utils.ReadWriteData import read_data
from Utils.ReadWriteData import write_data
from Utils.Algorithm import dijkstra_algorithm
from Utils.Graph import Graph


def main():
    n, m, users, graph = read_data('gamsrv.in')
    min_max_delay = None
    for vertex in graph.connections:
        if vertex not in users:
            current_delays = dijkstra_algorithm(graph, vertex)
            current_max_delay = max([current_delays[user] for user in users])
            if min_max_delay is None:
                min_max_delay = current_max_delay
            elif current_max_delay < min_max_delay:
                min_max_delay = current_max_delay

    write_data('gamsrv.out', min_max_delay)

    return min_max_delay


if __name__ == '__main__':
    print(main())

