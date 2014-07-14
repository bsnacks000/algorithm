# Prim's Minimum Spanning Tree Algorithm. O(mn) implementation. Not using heaps for optimization.

import sys

inputfile = sys.argv[1]

print 'Reading input...'

edges = {}
with open(inputfile, 'r') as reader:
  firstline = True
  for line in reader:
    fs = line.strip().split()
    if firstline:
      num_nodes = int(fs[0])
      num_edges = int(fs[1])
      firstline = False
      continue
    start_node = fs[0]
    end_node = fs[1]
    weight = int(fs[2])
    edge_key = start_node + ' ' + end_node
    edges[edge_key] = weight

print 'Startig Prim\'s MST algorithm...'

sum_cost = 0
spanned_nodes = {'1': 1}

while len(spanned_nodes) < num_nodes:
  min_weight = sys.maxint
  min_weight_target_node = None
  for edge_key in edges:
    node1, node2 = edge_key.split()
    weight = edges[edge_key]
    if weight < min_weight and ((node1 in spanned_nodes) != (node2 in spanned_nodes)):
      min_weight = weight
      if node1 in spanned_nodes:
        min_weight_target_node = node2
      else:
        min_weight_target_node = node1
  sum_cost += min_weight
  if min_weight_target_node == None:
    print 'No spannable node is found.'
    raise
  spanned_nodes[min_weight_target_node] = 1
  if len(spanned_nodes) % 10 == 0:
    print 'Spanned nodes:', len(spanned_nodes)

print 'Sum(cost):', sum_cost
