from math import gcd
from collections import deque

def solution(arr):
    answer = 0
    
    q = deque(arr)
    
    def lcm(x, y):
        return x * y // gcd(x, y)
    
    # 하나 남을때 까지
    while len(q) >= 2:
        x = q.popleft()
        y = q.popleft()
        
        answer = lcm(x, y)
        q.append(answer)
    
    return answer