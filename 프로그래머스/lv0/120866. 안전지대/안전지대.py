from itertools import product 

def solution(board):
    answer = 0
    
    boundary = list(product([-1, 0, 1], [-1, 0, 1]))
    n = len(board)
    
    def mark_danger_zone(x, y):
        for nx, ny in boundary:
            if x + nx >= 0 and x + nx < n  and y + ny >= 0 and y + ny < n:
                if board[x + nx][y + ny] == 0:
                    board[x + nx][y + ny] = 2
        
    for x_index, x in enumerate(board):
        for y_index, point in enumerate(x):            
            if point == 1:
                mark_danger_zone(x_index, y_index)
            #  index를 기준으로 전후좌우대각선을 위험 지역(2)로 표시
    
    for x_index, x in enumerate(board):
        for y_index, point in enumerate(x):            
            if point == 0:
                answer += 1
            
    return answer