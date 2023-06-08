import sys
sys.setrecursionlimit(10000)

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

def dfs(v):
  visited[v] = True
  for i in graph[v]:
    if not visited[i]:
      visited[i] = True
      dfs(i)

answer = 0

for i in range(1, n + 1):
  if not visited[i]:
    dfs(i)
    answer += 1

print(answer)