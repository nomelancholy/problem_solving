def solution(n):
    
    arr = []
    
    for i in range(n + 1):
        if i and n % i == 0:
            arr.append(i)
    
    answer = sum(arr)
    
    return answer