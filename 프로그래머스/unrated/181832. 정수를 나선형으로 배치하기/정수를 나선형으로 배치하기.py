def solution(n):
    
    answer = [[0 for _ in range(n)] for _ in range(n)] 
    
    r = 0
    c = 0
    number = 2
    
    answer[r][c] = 1 
    
    while number <= n ** 2:
        while c + 1 < n and answer[r][c + 1] == 0:
            c += 1            
            answer[r][c] = number
            number += 1
        
        while r + 1 < n and answer[r + 1][c] == 0:
            r += 1
            answer[r][c] = number
            number += 1
        
        while c - 1 >= 0 and answer[r][c - 1] == 0:
            c -= 1
            answer[r][c] = number
            number += 1
        
        while r - 1 >= 0 and answer[r - 1][c] == 0:
            r -= 1
            answer[r][c] = number
            number += 1
            
    return answer