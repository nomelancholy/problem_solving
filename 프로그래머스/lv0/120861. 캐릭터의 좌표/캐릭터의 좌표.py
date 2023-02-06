def solution(keyinput, board):
    answer = [0 , 0]
    
    w = board[0] // 2 
    h = board[1] // 2
    
    directions = ['up', 'down', 'left', 'right']
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    for key in keyinput:
        key_index = directions.index(key)
        
        x, y = dx[key_index], dy[key_index]
        nx, ny = answer[0], answer[1]
        
        if nx + x >= -w and nx + x <= w and ny + y >= -h and ny + y <= h:
            answer[0] = nx + x
            answer[1] = ny + y
            
    return answer