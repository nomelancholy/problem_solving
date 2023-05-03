def solution(strArr):
    answer = []
    
    for i, str in enumerate(strArr):
        if i % 2 == 1:
            answer.append(str.upper())
        else:
            answer.append(str.lower())
    
    return answer