from math import inf
from utils.printing import print_matrix
from utils.matrix import add_ones


def floyd_washall(adjacency_matrix):
    '''
    adjacency_matrix represents a weighted graph
    '''
    number_of_vertices = len(adjacency_matrix)
    dp = adjacency_matrix
    predecessor = [[None if i == j or dp[i][j] == inf else i
        for j in range(number_of_vertices)]
        for i in range(number_of_vertices)
    ]
    print_matrix(dp, 0)
    for k in range(number_of_vertices):
        new_dp = [[0] * number_of_vertices for _ in range(number_of_vertices)]
        new_predecessor = [[None] * number_of_vertices for _ in range(number_of_vertices)]
        for i in range(number_of_vertices):
            for j in range(number_of_vertices):
                if dp[i][k] + dp[k][j] < dp[i][j]:
                    new_dp[i][j] = dp[i][k] + dp[k][j]
                    new_predecessor[i][j] = predecessor[k][j]
                else:
                    new_dp[i][j] = dp[i][j]
                    new_predecessor[i][j] = predecessor[i][j]
        dp, predecessor = new_dp, new_predecessor
        print_matrix(dp, k + 1)
    add_ones(predecessor)
    return dp, predecessor
