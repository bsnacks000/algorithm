# Stanford Algorithm Analysis Part II Week 3 Programming Assignments 1 & 2
# Knapsack problem
import sys

sys.setrecursionlimit(10000)
file_name = sys.argv[1]

items = []
print 'Reading input...'
with open(file_name, 'r') as reader:
  first_line = True
  for line in reader:
    if first_line:
      first_line = False
      knapsack_size, num_of_items = [int(x) for x in line.strip().split()]
      continue
    value, weight = [int(x) for x in line.strip().split()]
    items.append((value, weight))

assert num_of_items == len(items)
print 'Read %d items.' % len(items)

optimals = [{} for x in range(num_of_items)]  # [right_most_item][weight_limit] = optimal_value

def get_optimal_value(right_most_item, weight_limit):
  global optimals

  # edge case 1
  if right_most_item < 0:
    return 0

  # edge case 2
  val, weight = items[right_most_item]
  if weight > weight_limit:
    return get_optimal_value(right_most_item - 1, weight_limit)

  # check cached case
  if weight_limit in optimals[right_most_item]:
    return optimals[right_most_item][weight_limit]

  # regular case
  val_with_this = get_optimal_value(right_most_item - 1, weight_limit)
  val_without_this = get_optimal_value(right_most_item - 1, weight_limit - weight) + val
  optimal_val =  max(val_with_this, val_without_this)
  optimals[right_most_item][weight_limit] = optimal_val
  return optimal_val

print 'Calculating optimal value...'
optimal_val = get_optimal_value(num_of_items - 1, knapsack_size)
print 'Optimal value:', optimal_val
