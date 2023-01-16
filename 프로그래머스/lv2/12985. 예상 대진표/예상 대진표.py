from collections import deque

def solution(n,a,b):
    answer = 1 
    
    # 계산 편의를 위해 x 가 y보다 항상 작게 만든다
    x = min(a, b)
    y = max(a, b)
    
    while True:
        xv, xr = divmod(x, 2)
        yv, yr = divmod(y, 2)
        
        if xv + xr == yv + yr:
            break
        
        if x % 2 == 1:
            x = (x + 1) // 2
        else:
            x = x // 2
        if y % 2 == 1:
            y = (y + 1) // 2
        else:
            y = y // 2
        answer += 1
    
    return answer