def solution(x, n):
    answer = []
    
    number = 0
    
    for i in range(n):
        number += x
        answer.append(number)
    
    return answer