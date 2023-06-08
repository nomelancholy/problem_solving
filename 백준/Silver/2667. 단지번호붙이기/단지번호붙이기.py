n = int(input())

graph = []
section_counts = []

for _ in range(n):
  graph.append(list(map(int, list(input()))))

def dfs(r, c):
  
  if r < 0 or c < 0 or r >= n or c >= n:
    return False
  if graph[r][c] == 1:
    global count
    count += 1
    
    graph[r][c] = 0
    dfs(r - 1, c)
    dfs(r + 1, c)
    dfs(r, c - 1)
    dfs(r, c + 1)
    
    return True
  return False

count = 0
result = 0

for i in range(n):
  for j in range(n):
    if dfs(i, j) == True:
      result += 1
      section_counts.append(count)
      count = 0

print(result)

section_counts.sort()

for section_count in section_counts:
  print(section_count)