# Dijkstra shortest path algorithm.
# Undirected weighted graph.
# For the sake of simplicity, heap is not used for keeping vertices to be added
# Usage: input, max_node_index, target_nodes
#        target_nodes are the nodes you want to display shortest path lengths for
#        target_nodes should be specified like 1,3,6,7
import sys
import heapq

input_path = sys.argv[1]
max_node_index = int(sys.argv[2])
report_target_nodes_str = sys.argv[3]
report_target_nodes = [int(x) for x in report_target_nodes_str.split(',')]

print 'Reading graph ...'
graph = [{} for x in range(max_node_index + 1)]  # [source][target] = weight
with open(input_path, 'r') as reader:
  for line in reader:
    fs = line.strip().split()
    source = int(fs[0])
    for i in range(1, len(fs)):
      target, weight = [int(x) for x in fs[i].split(',')]
      graph[source][target] = weight

print "Running Dijkstra's algorithm ..."
# X: lengths of known shortest paths from node 1
X = [sys.maxint] * (max_node_index + 1)  # [node], index 0 unused
X[1] = 0
unreached_nodes = {x:1 for x in range(2, max_node_index + 1)}
last_reached_node = 1
while len(unreached_nodes) > 0:
  for target in graph[last_reached_node]:
    X[target] = min(X[target], X[last_reached_node] + graph[last_reached_node][target])
  node_to_reach = None
  node_to_reach_distance = sys.maxint
  for node in unreached_nodes.keys():
    if X[node] < node_to_reach_distance:
      node_to_reach = node
      node_to_reach_distance = X[node_to_reach]
  unreached_nodes.pop(node_to_reach)
  last_reached_node = node_to_reach

distance_report = [str(X[x]) for x in report_target_nodes]
print ','.join(distance_report)
