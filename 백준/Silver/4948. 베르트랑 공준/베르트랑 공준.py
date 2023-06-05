import math

candidates = []

while True:
  n = int(input())
  
  if n == 0:
    break

  candidates.append(n)

sieve = [True for i in range(max(candidates) * 2 + 1)]

for i in range(2, int(math.sqrt(max(candidates) * 2)) + 1):
  if sieve[i] == True:
    multiple = 2
    while i * multiple <= max(candidates) * 2:
      sieve[i * multiple] = False
      multiple += 1

for candidate in candidates:
  print(sieve[candidate + 1: 2 * candidate 
+ 1].count(True))