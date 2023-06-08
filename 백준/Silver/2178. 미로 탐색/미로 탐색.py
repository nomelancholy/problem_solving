from collections import deque

n, m = map(int, input().split())

board = []

for _ in range(n):
  board.append(list(map(int, list(input()))))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c): 

  queue = deque()
  queue.append((r, c))

  while queue:
    r, c = queue.popleft()
    for i in range(4):
      nr = r + dr[i]
      nc = c + dc[i]

      if nr < 0 or nc < 0 or nr >= n or nc >= m or board[nr][nc] == 0:
        continue

      if board[nr][nc] == 1:
        board[nr][nc] = board[r][c] + 1
        queue.append((nr, nc))

  return board[n-1][m-1]

print(bfs(0, 0))