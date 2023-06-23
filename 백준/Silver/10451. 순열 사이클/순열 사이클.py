t = int(input())

def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]
  
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

for _ in range(t):
  n = int(input())
  
  graph = [0] + list(map(int, input().split()))
  parent = [i for i in range(n + 1)]

  count = 0
  for a, b in enumerate(graph):
    if a == 0:
      continue
    if find_parent(parent, a) == find_parent(parent, b):
      count += 1
    else:
      union_parent(parent, a, b)

  print(count)