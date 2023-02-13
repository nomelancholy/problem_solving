def solution(n, lost, reserve):
    
    _lost = list(set(lost) - set(reserve))
    _reserve = list(set(reserve) - set(lost))
    
    answer = n - len(_lost)
    
    for r in _reserve[:]:
        v = 0
        
        if (r - 1 in _lost):
            v = r - 1
        elif (r + 1 in _lost):
            v = r + 1
        
        if v != 0:
            answer += 1
            _reserve.remove(r)
            _lost.remove(v)
            
    return answer