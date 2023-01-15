def solution(a, b):
    
    if b < a:
        a, b = b, a
    
    arr = [i for i in range(a, b + 1)]
    answer = sum(arr)
    return answer