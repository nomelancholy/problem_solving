dr = [1, -1, 0, 0, 1, 1, -1, -1]
dc = [0, 0, 1, -1, 1, -1, 1, -1]

def dfs(r, c, graph, visited):
  visited[r][c] = True

  for i in range(len(dr)):
    nr = r + dr[i]
    nc = c + dc[i]

    if nr < 0 or nc < 0 or nr >= len(visited) or nc >= len(visited[0]):
      continue
    if visited[nr][nc]:
      continue
    if graph[nr][nc] == 1:
      dfs(nr, nc, graph, visited)
  
while True:
  w, h = map(int, input().split())
  visited = [[False] * w for _ in range(h)]
  answer = 0
  if w == 0 and h == 0:
    break
  graph = []
  for _ in range(h):
    graph.append(list(map(int, input().split())))

  for i in range(h):
    for j in range(w):
      if graph[i][j] == 1 and not visited[i][j]:
        dfs(i, j ,graph, visited)
        answer += 1

  print(answer)