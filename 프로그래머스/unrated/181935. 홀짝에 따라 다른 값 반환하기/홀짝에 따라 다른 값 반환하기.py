def solution(n):
    answer = 0
    
    if n % 2 == 1:
        answer = sum([i if i % 2 == 1 else 0 for i in range(n + 1)])
    else:
        answer = sum([i ** 2 if i % 2 == 0 else 0 for i in range(n + 1)])
        
    return answer