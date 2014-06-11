# Computes strongly connected component from a directed graph
# input vertices are integers that start from 1

import sys

inputfile = sys.argv[1]
N = int(sys.argv[2])  # max vertex index

print 'reading the graph...'
graph = [[] for i in range(N + 1)]  # [source] = [target, ...]
rev_graph = [[] for i in range(N + 1)]  # a graph with reversed edges
with open(inputfile, 'r') as fin:
  for line in fin:
    source, target = line.strip().split()
    source = int(source)
    target = int(target)
    graph[source] += [target]
    rev_graph[target] += [source]

# 1st round DFS starts
print 'doing 1st round DFSs...'
visited = [False] * (N + 1)
num_visited = 0

# records the nodes indices in the order of being "finished"
# the 0th element is unused
finished = [0] * (N + 1)
next_finished_index = 1

# todo stack
# [(node, next_neighbor)]
# next_neighbor is the index of the next neighbor in the neighbor list of this particular node
todo = []

# To be consistent with the video lecture, counting from N down to 1
for i in range(N, 0, -1):
  if visited[i]:
    continue
  todo.append((i, 0))
  while len(todo) > 0:
    node, next_neighbor_index = todo.pop()
    if not visited[node]:
      visited[node] = True
      num_visited += 1
      if num_visited % 10000 == 0:
        print 'visited', num_visited
    is_finished = True
    for j in range(next_neighbor_index, len(graph[node])):
      if not visited[graph[node][j]]:
        todo.append((node, j + 1))
        todo.append((graph[node][j], 0))
        is_finished = False
        break
    if is_finished:
      finished[next_finished_index] = node
      next_finished_index += 1


# 2nd round DFS starts
print 'doing 2nd round DFSs...'

visited = [False] * (N + 1)
num_visited = 0

# Since we do not have to keep track of the finishing time, we just use a simple todo stack
todo = []

# the size of the top K connected components
K = 5
topK_cc_sizes = [0] * K

# We have to pick the start nodes in the reverse order of finishing time
for i in range(N, 0, -1):
  leader = finished[i]
  if visited[leader]:
    continue
  todo.append(leader)
  current_cc_size = 0
  while len(todo) > 0:
    node = todo.pop()
    if not visited[node]:
      visited[node] = True
      current_cc_size += 1
      num_visited += 1
      if num_visited % 10000 == 0:
        print 'visited', num_visited
    for neighbor in rev_graph[node]:
      if not visited[neighbor]:
        todo.append(neighbor)
  if current_cc_size > topK_cc_sizes[K - 1]:
    topK_cc_sizes = sorted(topK_cc_sizes + [current_cc_size], reverse=True)[:K]

print ','.join([str(x) for x in topK_cc_sizes])
print 'Done.'
