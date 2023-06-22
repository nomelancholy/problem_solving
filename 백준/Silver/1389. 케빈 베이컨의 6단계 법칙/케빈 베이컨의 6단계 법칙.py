from collections import defaultdict

INF = int(1e9)

n, m = map(int, input().split())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for r in range(n + 1):
  for c in range(n + 1):
    if r == c:
      graph[r][c] = 0
    

for _ in range(m):
  a, b = map(int, input().split())
  graph[a][b] = 1
  graph[b][a] = 1

for k in range(n + 1):
  for r in range(n + 1):
    for c in range(n + 1):
      graph[r][c] = min(graph[r][c], graph[r][k] + graph[k][c])

kevin_dict = defaultdict(int)

for person, numbers in enumerate(graph):
  kevin_dict[person] = sum(numbers[1:])

arr = [p for p, n in kevin_dict.items() if n == min(kevin_dict.values())]

print(arr[0])