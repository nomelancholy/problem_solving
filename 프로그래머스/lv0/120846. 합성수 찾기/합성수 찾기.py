import math

def solution(n):
    answer = 0
    
    if n == 1:
        return answer
    
    for i in range(2, n + 1):
        for j in range(2, int(math.sqrt(i) + 1)):
            if i % j == 0:
                answer += 1
                break
    
    return answer