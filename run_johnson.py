from shortest_path.all_pairs.johnson import johnson
from utils.examples import GRAPH

from pprint import pprint


print("Using Johnson's algorithm:")
shortest_distance, predecessor = johnson(GRAPH)
print('The final distance matrix is below:')
pprint(shortest_distance)
print('The final predecessor matrix is below:')
pprint(predecessor)
