def solution(myString):
    answer = []
    
    count = 0
    
    for c in myString:
        if c == 'x':
            answer.append(count)
            count = 0
        else:
            count += 1
    
    answer.append(count)
    
    return answer