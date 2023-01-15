def solution(arr):

    target = min(arr)
    arr.remove(target)
    
    answer = arr if arr else [-1]
    
    return answer