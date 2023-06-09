from collections import deque

n = int(input())

graph = [[] for _ in range(n + 1)]
parents = [0] * (n + 1)

for _ in range(n - 1):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

q = deque()

for vertex in graph[1]:
  q.append((vertex, 1))

while q:
  v, parent = q.popleft()
  parents[v] = parent

  for node in graph[v]:
    if node != parents[v]:
      q.append((node, v))

for i in range(2, len(parents)):
  print(parents[i])