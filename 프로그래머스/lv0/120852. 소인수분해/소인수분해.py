import math

def solution(n):
    answer = []
    
    while n != 1:
        for i in range(2, n + 1):
            if n % i == 0:
                if i not in answer:
                    answer.append(i)
                n //= i
                break
    
    return answer