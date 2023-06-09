from collections import deque

t = int(input())

dr = [1, 1, -1, -1, 2, 2, -2, -2]
dc = [2, -2, 2, -2, 1, -1, 1, -1]

for _ in range(t):
  l = int(input())
  
  sr, sc = map(int, input().split())
  tr, tc = map(int, input().split())

  visited = [[False] * l for _ in range(l )]
  visited[sr][sc] = True
  
  q = deque([(sr, sc, 0)])

  while q:
    r, c, move = q.popleft()
    
    if r == tr and c == tc:
      print(move)
      break

    for i in range(len(dr)):
      nr = dr[i] + r
      nc = dc[i] + c

      if nr < 0 or nc < 0 or nr >= l or nc >= l:
        continue
      if not visited[nr][nc]:
        visited[nr][nc] = True
        q.append((nr, nc , move + 1))