from shortest_path.all_pairs.extend_shortest_paths import extend_shortest_paths
from utils.printing import print_matrix


def slow(adjacency_matrix):
    '''
    Uses Dynamic Programming to solve the all-pairs shortest paths problem
    adjancency_matrix represents a weighted graph
    '''
    number_of_vertices = len(adjacency_matrix)
    dp = adjacency_matrix
    print_matrix(dp, 1)
    for i in range(2, number_of_vertices):
        dp = extend_shortest_paths(adjacency_matrix, dp)
        print_matrix(dp, i)
    return dp
