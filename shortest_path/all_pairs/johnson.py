from shortest_path.single_source.dijkstra import dijkstra
from shortest_path.single_source.bellman_ford import bellman_ford

from math import inf
from pprint import pprint


def johnson(adjancency_matrix):
    number_of_vertices = len(adjancency_matrix)
    h = bellman_ford(adjancency_matrix, None, [0] * number_of_vertices)
    if h == None: return None
    print(f'The values of h are {h}')
    print()
    for i in range(number_of_vertices):
        for j in range(number_of_vertices):
            if i == j or adjancency_matrix[i][j] == inf: continue
            adjancency_matrix[i][j] += h[i] - h[j]
    print('Below is the adjancency matrix of the reweighted graph:')
    pprint(adjancency_matrix)
    print()
    shortest_d = [[inf] * number_of_vertices for _ in range(number_of_vertices)]
    predecessor = [[None] * number_of_vertices for _ in range(number_of_vertices)]
    for i in range(number_of_vertices):
        i_shortest_d, i_predecessor = dijkstra(adjancency_matrix, i)
        shortest_d[i][:] = (d + h[j] - h[i] for j, d in enumerate(i_shortest_d))
        predecessor[i][:] = i_predecessor
    return shortest_d, predecessor
