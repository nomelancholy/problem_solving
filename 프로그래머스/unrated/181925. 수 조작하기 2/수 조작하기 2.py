def solution(numLog):
    answer = ''
    
    for index in range(1, len(numLog)):
        if numLog[index-1] + 1 == numLog[index]:
            answer += 'w'
        elif numLog[index-1] - 1  == numLog[index]:
            answer += 's'
        elif numLog[index-1] + 10 == numLog[index]:
            answer += 'd'
        else:
            answer += 'a'
    
    return answer