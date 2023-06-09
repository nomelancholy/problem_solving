import sys
sys.setrecursionlimit(10000)

n = int(input())

min_h = 101
max_h = 0

ground = []

answer = 1

def dfs(r, c):
  global virtual_ground
  virtual_ground[r][c] = -1

  dr = [1, -1, 0, 0]
  dc = [0, 0, 1, -1]

  for i in range(len(dr)):
    nr = r + dr[i]
    nc = c + dc[i]

    if nr < 0 or nc < 0 or nr >= n or nc >= n:
      continue

    if virtual_ground[nr][nc] == -1:
      continue
    
    dfs(nr, nc)

for _ in range(n):
  line = list(map(int, input().split()))
  min_h = min(min_h, min(line))
  max_h = max(max_h, max(line))
  ground.append(line)

for rain_h in range(min_h, max_h):
  count = 0
  virtual_ground = []
  for i in range(n):
    line = []
    for j in range(n):
      if ground[i][j] <= rain_h:
        line.append(-1)
      else:
        line.append(ground[i][j])
    virtual_ground.append(line)


  for r in range(n):
    for c in range(n):
      if virtual_ground[r][c] != -1:
        dfs(r, c)
        count += 1
  answer = max(answer, count)
print(answer)