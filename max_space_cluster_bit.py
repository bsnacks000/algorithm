# Stanford Algorithms Part 2: Week 2 Question 2
# Max-spacing k-clustering by using bit operations and hamming distance
#
# This particular problem is reduced to find all pairs with hamming distance 
# smaller than or equan to 2, and by apply union-find on all such pairs, look
# at the number of clusters. 
#
# Any larger number of clusters than obtained will result in a smaller 
# max-spacing as defined in the lecture.
#
# The correct answer for Question 1 is 106.
# For this question, 651 is an incorrect answer.
#
import sys
from union_find import UnionFind

input_file = sys.argv[1]

def bits2num(bits):
  num = 0
  for bit in bits:
    num = num << 1
    num = num | bit
  return num

def get_mask(bit_index, num_bits):
  num = 0
  for i in range(num_bits):
    num = num << 1
    if i != bit_index:
      num = num | 1
  return num

def get_hamming_distance(val1, val2):
  diff = val1 ^ val2
  distance = 0
  while diff != 0:
    if diff & 1 == 1:
      distance += 1
    diff = diff >> 1
  return distance

print 'Reading input...'
nodes = []
first_line = True
with open(input_file, 'r') as reader:
  for line in reader:
    if first_line:
      first_line = False
      num_node, num_bits = [int(x) for x in line.strip().split()]
      continue
    bits = [int(x) for x in line.strip().split()]
    num = bits2num(bits)
    nodes.append(num)
print 'Expected %d nodes. Read %d nodes'%(num_node, len(nodes))
assert num_node == len(nodes)

print 'Creating hash-tables...'
num_hashtables = num_bits * (num_bits - 1) / 2
hashtable = [{} for x in range(num_hashtables)]
cur_table = 0
for i in range(num_bits - 1):
  for j in range(i + 1, num_bits):
    mask1 = get_mask(i, num_bits)
    mask2 = get_mask(j, num_bits)
    mask = mask1 & mask2
    for k in range(num_node):
      val = nodes[k]
      masked_val = val & mask
      if masked_val in hashtable[cur_table]:
        hashtable[cur_table][masked_val].append(k)
      else:
        hashtable[cur_table][masked_val] = [k]
    cur_table += 1
    if cur_table % 10 == 0:
      print '%d | %d'%(cur_table, num_hashtables)

print 'Sorting edges...'
cur_table = 0
edges = {i:set() for i in range(3)}  # [distance] = set(edge)
for ht in hashtable:
  for k, v in ht.items():
    if len(v) < 2:
      continue
    for i in range(len(v) - 1):
      for j in range(i + 1, len(v)):
        distance = get_hamming_distance(nodes[v[i]], nodes[v[j]])
        edge = '%d %d'%(v[i], v[j])
        edges[distance].add(edge)
  cur_table += 1
  if cur_table % 10 == 0:
    print '%d | %d'%(cur_table, num_hashtables)

print 'Applying union-find: union...'
uf = UnionFind()
connected_nodes = set()
for distance in range(3):
  edge_set = edges[distance]
  print 'distance: %d, edge_set size: %d'%(distance, len(edge_set))
  count_edge = 0
  for edge in edge_set:
    node1, node2 = edge.split()
    uf.union(node1, node2)
    connected_nodes.add(node1)
    connected_nodes.add(node2)
    count_edge += 1
    if count_edge % 100 == 0:
      print count_edge

print 'Applying union-find: find...'
root_set = set()
num_cluster = 0
cur_node = 0
for i in range(num_node):
  node = str(i)
  if node in connected_nodes:
    root = uf[node]
    if not root in root_set:
      root_set.add(root)
      num_cluster += 1
  else:
    num_cluster += 1
  cur_node += 1
  if cur_node % 1000 == 0:
    print '%d | %d'%(cur_node, num_node)

print 'Found %d clusters.'%num_cluster
