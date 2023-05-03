def solution(a, b):
    a_first_int = int(str(a) + str(b))
    b_first_int = int(str(b) + str(a))
    
    if a_first_int >= b_first_int:
        answer = a_first_int
    else:
        answer = b_first_int
        
    return answer