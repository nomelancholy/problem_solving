from itertools import combinations

def solution(balls, share):
    
    
    n = [i for i in range(1, balls + 1)]
    r = [i for i in range(1, share + 1)]
    nmr = [i for i in range(1, balls-share + 1)]
    
    n = 1
    r = 1
    nmr = 1
    
    for i in range(1, balls + 1):
        n *= i
    
    for i in range(1, share + 1):
        r *= i
        
    for i in range(1, balls - share + 1):
        nmr *= i
    
    answer = n // (r * nmr)
    
    return answer