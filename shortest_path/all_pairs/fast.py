from shortest_path.all_pairs.extend_shortest_paths import extend_shortest_paths
from utils.printing import print_matrix


def fast(adjacency_matrix):
    '''
    Uses Dynamic Programming to solve the all-pairs shortest paths problem
    adjacency_matrix represents a weighted graph
    '''
    number_of_vertices = len(adjacency_matrix)
    dp = adjacency_matrix
    i = 1
    print_matrix(dp, i)
    while i < number_of_vertices - 1:
        dp = extend_shortest_paths(dp, dp)
        i <<= 1
        print_matrix(dp, i)
    return dp
