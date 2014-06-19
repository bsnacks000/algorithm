import sys
import heapq

input_path = sys.argv[1]
numbers = []
with open(input_path, 'r') as reader:
  for line in reader:
    numbers.append(int(line.strip()))

msum = 0

maxheap = []  # smaller numbers
minheap = []  # bigger numbers

# initialize the first two numbers
if numbers[0] <= numbers[1]:
  msum += numbers[0] * 2
  maxheap.append(-numbers[0])
  minheap.append(numbers[1])
else:
  msum += numbers[0] + numbers[1]
  maxheap.append(-numbers[1])
  minheap.append(numbers[0])

# start maintaining the heaps
for i in range(2, len(numbers)):
  n = numbers[i]
  m1 = -maxheap[0]
  m2 = minheap[0]
  # print n, m1, m2, sorted(maxheap), sorted(minheap)
  
  if n >= m2:
    heapq.heappush(minheap, n)
  else:
    heapq.heappush(maxheap, -n)

  if len(maxheap) == len(minheap) + 2:
    heapq.heappush(minheap, -heapq.heappop(maxheap))
  elif len(maxheap) == len(minheap) - 1:
    heapq.heappush(maxheap, -heapq.heappop(minheap))

  median = -maxheap[0]
  msum += median

  if i < 20:
    j = i + 1
    tmp = sorted(numbers[:j])
    true_median = tmp[(j-1)/2]
    print sorted(numbers[:j]), median, true_median

print msum % 10000
