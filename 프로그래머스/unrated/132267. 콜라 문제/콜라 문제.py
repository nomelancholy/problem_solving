def solution(a, b, n):
    answer = 0
    
    while n >= a:
        received = n // a * b
        answer += received
        n = (n % a) +  received

    return answer