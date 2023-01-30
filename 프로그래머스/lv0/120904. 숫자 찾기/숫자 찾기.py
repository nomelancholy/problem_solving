def solution(num, k):
    answer = 0
    
    str_list = list(str(num))
    str_k = str(k)
    
    if str_k in str_list:
        answer = str_list.index(str_k) + 1
    else:
        answer = -1
    
    return answer