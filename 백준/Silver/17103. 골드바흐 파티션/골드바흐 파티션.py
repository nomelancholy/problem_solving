import math

t = int(input())

candidates = []

for _ in range(t):
  n = int(input())
  candidates.append(n) 

sieve = [True for i in range(max(candidates) + 1)]

sieve[0] = False
sieve[1] = False

for i in range(2, int(math.sqrt(max(candidates))  ) + 1):
  if sieve[i] == True:
    multiple = 2
    while i * multiple <= max(candidates):
      sieve[i * multiple] = False
      multiple += 1

for candidate in candidates:
  count = 0
  sum_set = set()
  
  for i in range(1, candidate + 1):
    diff = candidate - i
    if sieve[i] and sieve[diff]:
      if i not in sum_set and diff not in sum_set:
        sum_set.add(i)
        sum_set.add(diff)
        
        count += 1

  print(count)