import sys
import heapq

INF = int(1e9)
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
prev_node = [0] * (n + 1)

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))

s, e = map(int, input().split())

def dijkstra(start):
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
        prev_node[next_node] = now
        heapq.heappush(q, (cost, next_node))

dijkstra(s)
print(distance[e])
path = []

now = e

while now != s:
  path.append(now)
  now = prev_node[now]

path.append(now)

print(len(path))

for p in path[::-1]:
  print(p, end = ' ')