from utils.printing import print_matrix


def floyd_washall(adjacency_matrix):
    '''
    adjancency_matrix represents a weighted graph
    '''
    number_of_vertices = len(adjacency_matrix)
    dp = adjacency_matrix
    print_matrix(dp, 0)
    for k in range(number_of_vertices):
        dp = [[min(dp[i][j], dp[i][k] + dp[k][j])
            for j in range(number_of_vertices)]
            for i in range(number_of_vertices)
        ]
        print_matrix(dp, k + 1)
    return dp
