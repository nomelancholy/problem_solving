def solution(n):
    answer = 0
    
    
    
    # n이 1일 경우 1
    if n == 1:
        return 1
    # n이 2일 경우 2
    if n == 2:
        return 2

    dp = [0] * (n + 1)
    # n이 0일 경우 (계산 편의를 위해) 1일 경우와 2일 경우 저장
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n + 1):
        dp[i] = dp[i-2] + dp[i - 1]

    answer = dp[n] % 1234567
    
    return answer