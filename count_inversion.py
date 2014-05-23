#!/usr/bin/env python
# Count the number of inversions in a given array
# Input: array (one number per line)
# Output (STDOUT): number of inversions

import sys

# Sort and count the number of inversions
# arguments: start inclusive, end exclusive
# returns: number of inversions
def sort_count(arr, start, end):
  mid = start + (end - start) / 2
  if end <= start + 1:
    return 0
  inv1 = sort_count(arr, start, mid)
  inv2 = sort_count(arr, mid, end)
  i = start
  j = mid
  inv_this = 0
  tmp_arr = [0] * (end - start)
  pointer = 0
  while i < mid and j < end:
    if arr[i] < arr[j]:
      tmp_arr[pointer] = arr[i]
      i += 1
      pointer += 1
    else:
      tmp_arr[pointer] = arr[j]
      j += 1
      pointer += 1
      inv_this += j - (pointer + start)

  if j == end:
    while i < mid:
      tmp_arr[pointer] = arr[i]
      i += 1
      pointer += 1

  for t in range(0, pointer):
    arr[start + t] = tmp_arr[t]

  return inv1 + inv2 + inv_this

# Main
arr = []
for line in sys.stdin:
  line = line.strip()
  if len(line) == 0:
    continue
  num = int(line)
  arr.append(num)
arrlen = len(arr)
print "Read", arrlen, "integers."

print "Sort and counting."
num_inv = sort_count(arr, 0, len(arr))

print "Validating sorted array."
success = True
for i in range(len(arr)-1):
  if arr[i] > arr[i+1]:
    success = False
    print "Failed. arr[%d] = %d > arr[%d] = %d"%(i, arr[i], i+1, arr[i+1])

if success:
  print "Succeeded."

print "Number of inversions:", num_inv
