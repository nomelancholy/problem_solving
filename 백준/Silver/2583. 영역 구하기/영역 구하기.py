import sys
sys.setrecursionlimit(10000)

m, n, k = map(int, input().split())
board = [[0] * n for _ in range(m)]

section_count = 0
areas = []

for _ in range(k):
  lbc, lbr, rtc, rtr = map(int, input().split())
  for r in range(lbr, rtr):
    for c in range(lbc, rtc):
      board[r][c] = -1

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def dfs(r, c):
  global area
  board[r][c] = -1
  
  for i in range(len(dr)):
    nr = dr[i] + r
    nc = dc[i] + c

    if nr < 0 or nc < 0 or nr >= m or nc >= n:
      continue
    if board[nr][nc] == 0:
      dfs(nr, nc)
      area += 1
  
area = 1

for i in range(m):
  for j in range(n):
    if board[i][j] == 0:
      dfs(i, j)
      areas.append(area)
      section_count += 1
      area = 1

print(section_count)

areas.sort()

for area in areas:
  print(area, end=' ')