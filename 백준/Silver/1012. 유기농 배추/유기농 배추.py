import sys
sys.setrecursionlimit(10000)

def dfs(r, c):
  if r < 0 or c < 0 or r >= n or c >= m:
    return False
  if ground[r][c] == 0:
    return False

  if ground[r][c] == 1:
    ground[r][c] = 0
    dfs(r + 1, c)
    dfs(r - 1, c)
    dfs(r, c + 1)
    dfs(r, c - 1)
    return True
  return False

t = int(input())

for _ in range(t):
  
  answer = 0
  
  m, n, k = map(int, input().split())
  ground = [[0 for _ in range(m)] for _ in range(n)]
  
  for _ in range(k):
    x, y = map(int, input().split())
    ground[y][x] = 1

  for i in range(n):
    for j in range(m):
      if dfs(i, j):
        answer += 1

  print(answer)
  