# Week 6 Problem Assignment 1
import sys
import bisect
input_path = sys.argv[1]

numbers = [0] * 1000000

print 'reading input...'
i = 0
with open(input_path, 'r') as reader:
  for line in reader:
    number = int(line.strip())
    numbers[i] = number
    i += 1

print 'sorting...'
numbers = sorted(numbers)

print 'calculating...'
hits = {t:0 for t in range(-10000, 10001)}
processed = 0
for x in numbers:
  y_min = -10000 - x
  y_min_index = bisect.bisect_left(numbers, y_min)
  y_max = 10000 - x
  y_max_index = bisect.bisect_right(numbers, y_max)
  
  for i in range(y_min_index, y_max_index):
    y = numbers[i]
    if x != y:
      hits[x + y] = 1

  processed += 1
  if processed % 10000 == 0:
    print processed

print sum(hits.values())
