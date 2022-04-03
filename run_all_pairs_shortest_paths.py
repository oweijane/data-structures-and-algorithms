from utils.examples import GRAPH
from shortest_path.all_pairs.slow import slow
from shortest_path.all_pairs.fast import fast
from shortest_path.all_pairs.floyd_warshall import floyd_washall

from pprint import pprint


print('Using slow dynamic programming approach O(V^4) time:')
slow(GRAPH)

print('Using fast dynamic programming approach O(V^3 lgV) time:')
fast(GRAPH)

print('Using Floyd-Warshall algorithm O(V^3) time:')
tmp = floyd_washall(GRAPH)
print('The final predecessor matrix is below:')
pprint(tmp[1])
