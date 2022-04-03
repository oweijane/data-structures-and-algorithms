from shortest_path.all_pairs.extend_shortest_paths import extend_shortest_paths
from pprint import pprint


def print_matrix(dp, i):
    print(i)
    pprint(dp)
    print()


def slow_all_pairs_shortest_path(adjacency_matrix):
    '''
    adjancency_matrix represents a weighted graph
    '''
    number_of_vertices = len(adjacency_matrix)
    dp = adjacency_matrix
    print_matrix(dp, 1)
    for i in range(2, number_of_vertices):
        dp = extend_shortest_paths(adjacency_matrix, dp)
        print_matrix(dp, i)
    return dp
