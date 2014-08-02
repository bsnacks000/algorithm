import sys

def add_edge(graph, source, target, weight):
  if not source in graph:
    graph[source] = {}
  graph[source][target] = weight

input_file = sys.argv[1]

first_line = True
graph = {}
invgraph = {}
with open(input_file) as reader:
  for line in reader:
    if first_line:
      first_line = False
      num_node, num_edge = map(int, line.strip().split())
      continue
    source, target, weight = map(int, line.strip().split())
    add_edge(graph, source, target, weight)
    add_edge(invgraph, target, source, weight)

node_set = set(graph.keys() + invgraph.keys())
node_list = list(node_set)

assert num_node == len(node_list)

# Complete graph matrix
for node in node_list:
  if not node in graph:
    graph[node] = {}

cost_matrix = {}

# Base case
for source in node_list:
  cost_matrix[source] = {}
  for target in node_list:
    if target == source:
      cost_matrix[source][target] = 0
    elif target in graph[source]:
      cost_matrix[source][target] = graph[source][target]
    else:
      cost_matrix[source][target] = sys.maxint

for (i, k) in enumerate(node_list):
  new_cost_matrix = {}
  for source in node_list:
    new_cost_matrix[source] = {}
    for target in node_list:
      new_cost_matrix[source][target] = min(cost_matrix[source][target], cost_matrix[source][k] + cost_matrix[k][target])
  cost_matrix = new_cost_matrix
  print '%d / %d' % (i, num_node)

# Check negative-cost cycle
has_negative_cycle = False
for node in node_list:
  if cost_matrix[node][node] < 0:
    has_negative_cycle = True
    break

if has_negative_cycle:
  print 'Negative cycle detected.'
  sys.exit(0)

min_shortest_path = sys.maxint
for source in node_list:
  for target in node_list:
    if source == target:
      continue
    min_shortest_path = min(min_shortest_path, cost_matrix[source][target])

print 'Shortest shortest path =', min_shortest_path
