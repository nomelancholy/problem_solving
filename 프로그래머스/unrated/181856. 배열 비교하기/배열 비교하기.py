def solution(arr1, arr2):
    answer = 0
    
    if len(arr1) == len(arr2):
        if sum(arr1) > sum(arr2):
            answer = 1
        elif sum(arr2) > sum(arr1):
            answer = -1
        else:
            answer = 0
    else:
        if len(arr1) > len(arr2):
            answer = 1
        else:
            answer = -1
    
    return answer