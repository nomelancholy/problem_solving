from collections import defaultdict

n, m = map(int, input().split())

cant_here = set()
cant_see = set()

for _ in range(n):
  cant_here.add(input())

for _ in range(m):
  cant_see.add(input())

result = cant_here & cant_see
print(len(result))

for name in sorted(list(result)):
  print(name)