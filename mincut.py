#!/usr/bin/env python
# Using random contraction algorithm to calculate mincut
import sys
import random
import math
import copy

inputfile = sys.argv[1]
graph = {}  # [node][neighbor] = weight
with open(inputfile, 'r') as fin:
  for line in fin:
    fs = line.strip().split()
    source = int(fs[0])
    graph[source] = {}
    for i in range(1, len(fs)):
      target = int(fs[i])
      if target in graph[source]:
        graph[source][target] += 1
      else:
        graph[source][target] = 1

def add_to_dict(dict_, key, value):
  dict_[key] = dict_.setdefault(key, 0) + value

# Returns weight of the final single link
def random_contraction(graph):
  random.seed()
  while len(graph) > 2:
    source = random.sample(graph.keys(), 1)[0]
    target = random.sample(graph[source].keys(), 1)[0]
    # tot = target of target
    for tot in graph[target]:
      graph[tot].pop(target)
      if tot != source:
        add_to_dict(graph[source], tot, graph[target][tot])
        add_to_dict(graph[tot], source, graph[target][tot])
    graph.pop(target)
  return graph.values()[0].values()[0]

n = len(graph)
num_trials = int(n * n * math.log(n) / math.log(2))
print 'n = %d\nnum_trials = %d'%(n, num_trials)
mincut = None
for trial in range(num_trials):
  graph_copy = copy.deepcopy(graph)
  cut = random_contraction(graph_copy)
  if mincut == None:
    mincut = cut
  elif cut < mincut:
    mincut = cut
    print 'current mincut =', mincut, 'trial =', trial
print 'Finished.'
