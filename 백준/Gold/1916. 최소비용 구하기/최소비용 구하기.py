import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

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
    for target, target_cost in graph[now]:
      cost = dist + target_cost
      if distance[target] > cost:
        distance[target] = cost
        heapq.heappush(q, (cost, target))

dijkstra(s)
print(distance[e])