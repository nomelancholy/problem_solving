n = int(input())

graph = []

for _ in range(n):
  graph.append(list(map(int, input().split())))

for k in range(n):
  for r in range(n):
    for c in range(n):
      if graph[r][c] == 1 or (graph[r][k] == 1 and graph[k][c] ):
        graph[r][c] = 1

for line in graph:
  for number in line:
    print(number, end=' ')
  print()