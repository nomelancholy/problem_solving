def solution(num_list):
    answer = 0
    
    for i, x in enumerate(num_list):
        if x < 0:
            return i
    
    return -1