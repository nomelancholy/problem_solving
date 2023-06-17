n = int(input())

multitabs = []

for _ in range(n):
  multitabs.append(int(input()))

total = 0

multitabs.sort()

for i in range(n -1):
  total += multitabs[i] - 1

total += multitabs[-1]

print(total)