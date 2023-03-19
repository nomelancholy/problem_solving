from collections import deque

def dfs(graph, start, visited):

  # 현재 노드 방문 처리
  visited[start] = True

  print(start, end=' ')
  
  # 현재 노드와 연결된 다른 노드들 탐색
  for i in graph[start]:
    if not visited[i]:
      dfs(graph, i, visited)
  
def bfs(graph, start, visited):
  # 현재 노드 큐에 삽입하고 방문처리
  queue = deque([start])

  visited[start] = True

  # 큐가 빌 때 까지
  while queue:
    # 큐에 먼저 들어간 값을 뽑아
    visit = queue.popleft()
    # 출력하고
    print(visit, end=' ')
    # 해당 값과 인접한 노드들 중
    for i in graph[visit]:
      # 방문하지 않은 값이 있으면
      if not visited[i]:
        # 큐에 집어넣고
        queue.append(i)
        # 방문처리 한다
        visited[i] = True
  
# 정점 갯수, 간선 갯수, 시작 번호 입력 받음
n, m, v = map(int, input().split())

# 방문 여부 체크 리스트 정점 갯수 + 1 만큼 세팅 (0을 쓰지 않으니)
dfs_visited_list = [False] * (n + 1)
bfs_visited_list = [False] * (n + 1)

# 그래프 배열을 n + 1개만큼 가진 2차원 배열 형태로 세팅
graph = [[] for i in range(n + 1)]

# 간선 갯수만큼 반복하면서
for _ in range(m):
  # 입력받고
  i, j = map(int, input().split())
  # i의 위치에 j 추가 / j의 위치에 i 추가
  graph[i].append(j)
  graph[j].append(i)

for j in range(n+1):    # 끝까지 정렬 다하기!
    graph[j].sort()

# v부터 dfs 탐색 시작
dfs(graph, v, dfs_visited_list)

print()

# v부터 bfs 탐색 시작
bfs(graph, v, bfs_visited_list)