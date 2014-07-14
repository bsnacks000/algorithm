# Stanford Algorithms Part 2: Week 2 Question 1
# Max-spacing k-clustering
import sys
from union_find import UnionFind

k = 4  # number of clusters

input_file = sys.argv[1]

edges = {}
first_line = True
print 'Reading input...'
with open(input_file, 'r') as reader:
  for line in reader:
    if first_line:
      first_line = False
      num_node = int(line.strip())
      continue
    fs = line.strip().split()
    edge = fs[0] + ' ' + fs[1]
    cost = int(fs[2])
    edges[edge] = cost

print 'Finished reading. %d nodes, %d edges.'%(num_node, len(edges))

print 'Start clustering...'
num_cluster = num_node
max_spacing = -1
sorted_edges = sorted(edges.items(), key=lambda x: x[1])
edge_index = 0
uf = UnionFind()

while num_cluster >= k:
  edge, cost = sorted_edges[edge_index]
  edge_index += 1
  node1, node2 = edge.split()
  node1 = int(node1)
  node2 = int(node2)
  if node1 in uf and node2 in uf and uf[node1] == uf[node2]:
    continue
  uf.union(node1, node2)
  num_cluster -= 1
  max_spacing = cost
  if num_cluster % 10 == 0:
    print num_cluster, max_spacing

print 'Max spacing:', max_spacing