def solution(a, d, included):
    answer = 0
    
    for index, flag in enumerate(included):
        if flag:
            answer += a + d * index
            
    return answer