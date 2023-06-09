from collections import deque

m, n = map(int, input().split())

box = []
ripes = []

for x in range(n):
  line = list(map(int, input().split()))
  for y, tomato in enumerate(line):
    if tomato == 1:
      ripes.append((x, y, 0))
  box.append(line)

q = deque(ripes)

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

answer = 0

while q:
  r, c, day = q.popleft()
  answer = day
  for i in range(len(dr)):
    nr = r + dr[i]
    nc = c + dc[i]

    if nr < 0 or nc < 0 or nr >= n or nc >= m:
      continue
    if box[nr][nc] == 0:
      box[nr][nc] = 1
      q.append((nr, nc, day + 1))

for i in range(n):
  for j in range(m):
    if box[i][j] == 0:
      answer = -1

print(answer)