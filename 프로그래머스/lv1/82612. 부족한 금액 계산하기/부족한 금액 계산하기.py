def solution(price, money, count):

    fare = sum([i * price for i in range(1, count + 1)])
    answer = fare - money if fare - money > 0 else 0
    
    return answer