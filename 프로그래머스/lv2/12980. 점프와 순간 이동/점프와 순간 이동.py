def solution(n):
    ans = 0
    
    while n != 0:
        # 홀수
        if n % 2 == 1:
            n = n - 1
            ans += 1
        # 짝수
        else:
            n = n // 2

    return ans
