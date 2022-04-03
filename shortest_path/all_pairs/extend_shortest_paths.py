from math import inf


def extend_shortest_paths(adjancency_matrix, dp):
    number_of_vertices = len(adjancency_matrix)
    new_dp = [[inf] * number_of_vertices for _ in range(number_of_vertices)]
    for i in range(number_of_vertices):
        for j in range(number_of_vertices):
            for k in range(number_of_vertices):
                new_dp[i][j] = min(new_dp[i][j], dp[i][k] + adjancency_matrix[k][j])
    return new_dp
