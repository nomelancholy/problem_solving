def solution(n):
    answer = 1
    
    while True:
        fact = 1
        for i in range(1, answer + 1):
            fact *= i
        if fact > n:
            break
        else:
            answer += 1
        
    answer -= 1        
        
    return answer