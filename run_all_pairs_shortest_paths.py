from utils.examples import GRAPH
from shortest_path.all_pairs.slow import slow
from shortest_path.all_pairs.fast import fast


print('Using slow dynamic programing approach O(V^4) time:')
slow(GRAPH)

print('Using fast dynamic programing approach O(V^3 lgV) time:')
fast(GRAPH)
