def solution(babbling):
    answer = 0
    
    possible = ['aya',  'ma', 'woo', 'ye',]
    
    for b in babbling:
        remains = b
        for p in possible:
            remains = remains.replace(p, ' ')
            
        if remains.strip() == '':
            answer += 1
    
    return answer