def solution(s):
    answer = True
    
    p_count = 0
    y_count = 0
    
    s = s.lower()
    
    for c in s:
        if c == 'p':
            p_count += 1
        elif c == 'y':
            y_count += 1
    
    if p_count != y_count:
        answer = False
        
    return answer