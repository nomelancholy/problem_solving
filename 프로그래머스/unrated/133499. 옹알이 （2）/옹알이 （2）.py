def solution(babbling):
    answer = 0
    
    possible = ['aya', 'ye', 'woo', 'ma']
    
    for b in babbling:
        remains = b
        for p in possible:
            
            if remains.count(p) > 1:
                check_word = p * 2
                copy_remains = remains
                result = copy_remains.replace(check_word, '')
                
                if len(result) <= len(remains) - len(check_word):
                    break
                
            remains = remains.replace(p, ' ')
            
        if remains.strip() == '':
            answer += 1
    
    return answer