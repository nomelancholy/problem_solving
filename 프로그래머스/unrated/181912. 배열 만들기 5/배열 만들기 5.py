def solution(intStrs, k, s, l):
    answer = []
    
    for intStr in intStrs:
        convert = int(intStr[s:s + l])
        if k < convert:
            answer.append(convert)
        
    return answer