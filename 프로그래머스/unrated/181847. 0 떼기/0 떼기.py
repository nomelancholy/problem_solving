def solution(n_str):
    answer = ''
    flag = False
    
    for c in n_str:
        if c != '0':
            flag = True
            
        if flag:
            answer += c
            
    return answer