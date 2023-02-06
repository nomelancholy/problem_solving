def solution(dots):
    answer = 0
    
    l_set = set()
    w_set = set()
    
    for dot in dots:
        l_set.add(dot[0])
        w_set.add(dot[1])
        
    length = max(l_set) - min(l_set)
    width = max(w_set) - min(w_set)
    
    answer = length * width
    
    return answer