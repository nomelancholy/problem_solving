import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, e = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(e):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  graph[b].append((a, c))

v1, v2 = map(int, input().split())

def dijkstra(start):
  distance = [INF] * (n + 1)
  distance[start] = 0
  q = []
  heapq.heappush(q, (0, start))
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for next_node, next_dist in graph[now]:
      cost = dist + next_dist
      if cost < distance[next_node]:
        distance[next_node] = cost
        heapq.heappush(q, (cost, next_node))
  return distance

s_d = dijkstra(1)
v1_d = dijkstra(v1)
v2_d = dijkstra(v2)

answer = min(s_d[v1] + v1_d[v2] + v2_d[n], s_d[v2] + v2_d[v1] + v1_d[n])

if answer >= INF:
  print(-1)
else:
  print(answer)