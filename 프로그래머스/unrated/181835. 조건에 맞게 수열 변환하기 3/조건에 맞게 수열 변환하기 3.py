def solution(arr, k):
    
    if k % 2 == 0:
        return [k + n for n in arr]
    else:
        return [k * n for n in arr]
    