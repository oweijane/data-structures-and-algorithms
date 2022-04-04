from math import inf


def bellman_ford(adjacency_matrix, source):
    '''
    returns None if negative cycle exists
    adjacency_matrix represents a weighted graph
    '''
    number_of_vertices = len(adjacency_matrix)
    shortest_d = [inf] * number_of_vertices
    shortest_d[source] = 0
    for _ in range(number_of_vertices - 1):
        for i in range(number_of_vertices):
            for j in range(number_of_vertices):
                if i == j or adjacency_matrix[i][j] == inf: continue
                candidate_d = shortest_d[i] + adjacency_matrix[i][j]
                if candidate_d < shortest_d[j]:
                    shortest_d[j] = candidate_d
    # Checking for negative cycle
    for i in range(number_of_vertices):
        for j in range(number_of_vertices):
            if i == j or adjacency_matrix[i][j] == inf: continue
            candidate_d = shortest_d[i] + adjacency_matrix[i][j]
            if candidate_d < shortest_d[j]:
                return None
    return shortest_d
