from collections import deque

def solution(maps):
    answer = 0
    
    q = deque()
    q.append([0, 0])
    
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    
    while q:
        y, x = q.popleft()
        
        for i in range(4):
            ny = dy[i] + y                 
            nx = dx[i] + x
            
            # nx, ny 가 범위 안이고
            if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]):
                # 벽이거나 방문한 곳이 아니면
                if maps[ny][nx] == 0:
                    continue
                if maps[ny][nx] == 1:
                    # 큐에 넣고
                    q.append([ny, nx])
                    # 값 갱신
                    maps[ny][nx] = maps[y][x] + 1            
                
    answer = maps[-1][-1]
    
    if answer == 1:
        answer = -1
    
    return answer