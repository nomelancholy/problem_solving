def solution(my_string):
    
    arr = [c.lower() for c in my_string]
    
    arr.sort()

    answer = ''.join(arr)
    
    return answer