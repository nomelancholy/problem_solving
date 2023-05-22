def solution(myString):
    answer = []
    
    chunk = ''
    
    for c in myString:
        if c == 'x':
            if chunk != '':
                answer.append(chunk)
                chunk = ''
        else:
            chunk += c
    
    if chunk != '':
        answer.append(chunk)
            
    answer.sort()
    
    return answer