lines = list(map(int, input().split()))
lines.sort()

if lines[-1] < sum(lines[:2]):
  print(sum(lines))
else:
  longest = lines[-1]
  while longest >= sum(lines[:2]):
    longest -= 1
  print(sum(lines[:2]) + longest)