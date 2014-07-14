# Schedule jobs based on their weights and length, optimizing using two different strategies.
# Stanford Algorithm II Week 1 Programming Assignment 1 & 2

import sys
import functools

inputfile = sys.argv[1]
strategy = sys.argv[2]

print 'Reading input...'

jobs = []
with open(inputfile, 'r') as reader:
  first_line = True
  for line in reader:
    if first_line:
      first_line = False
      continue
    else:
      fs = line.strip().split()
      weight = int(fs[0])
      length = int(fs[1])
      jobs.append((weight, length))

print 'Sorting...'

if strategy == '1':
  def cmp_func(job1, job2):
    diff = (job2[0] - job2[1]) - (job1[0] - job1[1])
    if diff != 0:
      return diff
    else:
      return job2[0] - job1[0]
elif strategy == '2':
  def cmp_func(job1, job2):
    diff = (float(job2[0]) / job2[1]) - (float(job1[0]) / job1[1])
    if diff != 0:
      return diff
    else:
      return job2[0] - job1[0]
else:
  print 'Unknown strategy.'
  raise 

jobs_sorted = sorted(jobs, key=functools.cmp_to_key(cmp_func))

print 'Calculating weights...'
sum_weighted_completion_time = 0
last_completion_time = 0
for weight, length in jobs_sorted:
  last_completion_time += length
  sum_weighted_completion_time += weight * last_completion_time

print 'sum of weighted completion time:', sum_weighted_completion_time
