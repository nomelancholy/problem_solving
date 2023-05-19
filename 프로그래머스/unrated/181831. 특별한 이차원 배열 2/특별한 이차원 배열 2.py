def solution(arr):
    answer = 0
    
    rra = list(map(list, zip(*arr)))
    
    if arr == rra:
        answer = 1
        
    return answer