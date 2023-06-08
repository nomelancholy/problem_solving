import sys
sys.setrecursionlimit(10000)

n = int(input())

board = []
visited = [[False] * n for _ in range(n)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for _ in range(n):
  board.append(list(input()))

def dfs(r, c):

  current_color = board[r][c]
  visited[r][c] = True
  
  for i in range(4):
    nr = r + dr[i]
    nc = c + dc[i]

    if nr < 0 or nc < 0 or nr >= n or nc >= n:
      continue
    if visited[nr][nc]:
      continue    
    if board[nr][nc] == current_color:
      dfs(nr, nc)

normal_count = 0
colorless_count = 0

for i in range(n):
  for j in range(n):
    if not visited[i][j]:
      dfs(i, j)
      normal_count += 1

for i in range(n):
  for j in range(n):
    if board[i][j] == 'R':
      board[i][j] = 'G'

visited = [[False] * n for _ in range(n)]

for i in range(n):
  for j in range(n):
    if not visited[i][j]:
      dfs(i, j)
      colorless_count += 1

print(normal_count, end=' ')
print(colorless_count)