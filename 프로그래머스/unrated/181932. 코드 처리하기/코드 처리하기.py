def solution(code):
    answer = ''
    
    mode = 0
    
    for idx, c in enumerate(code):
        if c == '1':
            if mode == 0:
                mode = 1
            else:
                mode = 0
        else:
            if mode == 0:
                if idx % 2 == 0:
                    answer += c
            else:
                if idx % 2 == 1:
                    answer += c
                
    if answer:
        return answer
    else:
        return 'EMPTY'