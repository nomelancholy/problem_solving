def solution(x):

    arr = list(map(int, [n for n in str(x)]))
    sum_number = sum(arr)
    
    if x % sum_number == 0:
        return True
    else:
        return False