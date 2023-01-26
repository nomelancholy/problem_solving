import math

def solution(n):
    
    answer = math.sqrt(n).is_integer()
    
    if answer:
        answer = 1
    else:
        answer = 2
    
    return answer