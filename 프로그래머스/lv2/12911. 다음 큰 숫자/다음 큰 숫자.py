def solution(n):
    answer = 0
    
    target = n + 1
    bin_n = format(n, 'b')
    
    while True:
        bin_t = format(target, 'b')
        if bin_n.count('1') == bin_t.count('1'):
            answer = target
            break
        target += 1
        
    return answer