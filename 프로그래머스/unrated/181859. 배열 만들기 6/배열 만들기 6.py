def solution(arr):
    answer = []
    
    i = 0
    
    while i < len(arr):
        if answer:
            if arr[i] == answer[-1]:
                answer = answer[:-1]
                i += 1
            else:
                answer.append(arr[i])
                i += 1
        else:
            answer.append(arr[i])
            i += 1
    
    if answer:
        return answer
    else:
        return [-1]