def solution(n):
    
    arr = list(str(int(n)))
    arr.sort(reverse=True)
    
    answer = int(''.join(arr))
    
    return answer