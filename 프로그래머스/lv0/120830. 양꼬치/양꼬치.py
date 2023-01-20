def solution(n, k):
    meat = 12000
    drink = 2000
    service = n // 10
    answer = meat * n + drink * (k - service)
    return answer