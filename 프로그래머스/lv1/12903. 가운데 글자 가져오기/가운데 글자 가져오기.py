def solution(s):
    answer = ''
    
    i = len(s) // 2
    
    answer = s[i - 1:i + 1] if len(s) % 2 == 0 else s[i:i + 1]
        

    return answer