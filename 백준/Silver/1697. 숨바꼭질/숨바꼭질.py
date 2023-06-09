from collections import deque

def bfs(start, target, visited):
  depth = 0
  q = deque([(start, depth)])
  visited[start] = True

  while q:
    now, d = q.popleft()
    
    if now == target:
      print(d)
      break

    if 0 <= now - 1 <= 100000 and visited[now - 1] == False:
      visited[now - 1] = True
      q.append((now - 1, d + 1 ))
    if 0 <= now + 1 <= 100000 and visited[now + 1] == False:
      visited[now + 1] = True
      q.append((now + 1, d + 1 ))
    if 0 <= now * 2 <= 100000 and visited[now * 2] == False:
      visited[now * 2] = True
      q.append((now * 2, d + 1 ))      

n, k = map(int, input().split())
visited = [False] * 100001
bfs(n, k, visited)
