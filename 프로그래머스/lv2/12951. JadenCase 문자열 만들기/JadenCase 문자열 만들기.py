def solution(s):
    answer = ''
    
    first_flag = True
    
    for c in s:
        # 공백이면
        if c == ' ':
            if not first_flag:
                first_flag = True
            answer += c            
        # 글자면
        else:
            if first_flag:
                answer += c.upper()
                first_flag = False
            else:
                answer += c.lower()            

    return answer