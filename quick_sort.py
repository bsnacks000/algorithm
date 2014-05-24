#!/usr/bin/env python
# Quick sorting on array
# Input: array (one number per line)
# Output: number of comparisons
# see: https://class.coursera.org/algo-005/quiz/attempt?quiz_id=33

import sys

def swap(arr, i, j):
  tmp = arr[i]
  arr[i] = arr[j]
  arr[j] = tmp

# arguments: start inclusive, end exclusive, pilot_selection_method
# pivot_selection_method: 1 first, 2 final, 3 median-of-three
# returns the number of comparisons
def quick_sort(arr, start, end, method):
  if end <= start + 1:
    return 0
  
  # print "BEFORE SORT:", arr[start:end]

  # Choosing a pivot
  if method == 1:
    pivot = arr[start]
  elif method == 2:
    pivot = arr[end - 1]
    swap(arr, start, end-1)
  elif method == 3:
    candidates = {}  # [index] = value
    candidates[start] = arr[start]
    candidates[end-1] = arr[end-1]
    mid = start + (end - start - 1) / 2
    candidates[mid] = arr[mid]
    sorted_candidates = sorted(candidates.values())
    for i in candidates:
      if candidates[i] == sorted_candidates[1]:
        pivot = arr[i]
        swap(arr, start, i)
  else:
    raise Expcetion('Invalid method')

  # print "PIVOT CHOSEN:", arr[start:end]

  # Partition
  i = start + 1  # end of the first partition (exclusive)
  j = start + 1  # end of the second partition (exclusive)
  while j < end:
    if arr[j] >= pivot:
      j += 1
    else:
      swap(arr, i, j)
      i += 1
      j += 1

  # print "AFTER PARTITION:", arr[start:end]

  # Final swap
  swap(arr, start, i-1)
  pivot_position = i-1

  # print "FINAL SWAP DONE:", arr[start:end]
  # print

  # Recursive calls and sum up
  comparisons_this = end - start - 1
  comparisons_left = quick_sort(arr, start, pivot_position, method)
  comparisons_right = quick_sort(arr, pivot_position+1, end, method)
  return comparisons_this + comparisons_left + comparisons_right

# Main
arr_raw = []
for line in sys.stdin:
  line = line.strip()
  if len(line) == 0:
    continue
  num = int(line)
  arr_raw.append(num)
arrlen = len(arr_raw)
print "Read", arrlen, "integers."
print

sys.setrecursionlimit(arrlen * 10)

for method in range(1, 4):
  print "Sorting using method", method
  arr = list(arr_raw)
  num_comparisons = quick_sort(arr, 0, len(arr), method)

  print "Validating sorted array."
  success = True
  for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
      success = False
      print "Failed. arr[%d] = %d > arr[%d] = %d"%(i, arr[i], i+1, arr[i+1])

  if success:
    print "Succeeded."

  print "Number of comparisons:", num_comparisons
  print

