n = int(input())
m = int(input())

computers = [[] for _ in range(n + 1)]

visited = [False] * (n + 1)

for _ in range(m):
  x, y = map(int, input().split())

  computers[x].append(y)
  computers[y].append(x)

def dfs(v):
  visited[v] = True

  for computer in computers[v]:
    if visited[computer] == False:
      dfs(computer)
  
dfs(1)

print(visited.count(True)-1)