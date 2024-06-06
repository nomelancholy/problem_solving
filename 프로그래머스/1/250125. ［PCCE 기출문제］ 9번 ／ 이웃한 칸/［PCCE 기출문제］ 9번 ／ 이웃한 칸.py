def solution(board, r, c):
    answer = 0
    
    board_length = len(board[0])
    target_color = board[r][c]
    
    dr = [0, 1, -1 ,0]
    dc = [1, 0, 0, -1]
        
    for i in range(4):
        target_r = r + dr[i]
        target_c = c + dc[i]
        
        if 0 <= target_r < board_length and 0 <= target_c < board_length:
            if board[target_r][target_c] == target_color:
                answer += 1
    
    return answer