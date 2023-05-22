def solution(myString, pat):
    answer = ''
    
    index = 0
    
    for i in range(len(myString)):
        if myString[i:].startswith(pat):
            index = i
    
    answer = myString[:index + len(pat)]
    
    return answer