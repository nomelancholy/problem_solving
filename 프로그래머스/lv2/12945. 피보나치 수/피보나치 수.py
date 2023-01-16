def solution(n):
    
    memo = [0] * (n + 1)
    
    memo[1] = 1
    memo[2] = 1
    
    for i in range(3, n + 1):
        if not memo[i]:
            memo[i] = memo[i - 1] + memo[i - 2]
            
    answer = memo[n] % 1234567
            
    return answer