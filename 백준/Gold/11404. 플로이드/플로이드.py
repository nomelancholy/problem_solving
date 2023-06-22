INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for r in range(n + 1):
  for c in range(n + 1):
    if r == c:
      graph[r][c] = 0

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a][b] = min(graph[a][b], c)
  
for k in range(1, n + 1):
  for r in range(1, n + 1):
    for c in range(1, n + 1):
      graph[r][c] = min(graph[r][c], graph[r][k] + graph[k][c])

for i in range(1, n + 1):
  for cost in graph[i][1:]:
    if cost == INF:
      print(0, end=' ')
    else:
      print(cost, end=' ')
  print()