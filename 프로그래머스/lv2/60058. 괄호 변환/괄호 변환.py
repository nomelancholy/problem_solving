def solution(p):
    
    answer = ''
    
    # 1
    if not p:
        return ""
    
    # 올바른 괄호 문자열인지 판별
    def check_right(string):
        
        left = 0
        right = 0
        
        for c in string:
            if c == '(':
                left += 1
            else:
                right += 1
        
            if left < right:
                return False
        
        return True
    
    # 문자열 확인
    def check_string(string):
        
        completed_string = ''
        
        # 빈 문자열이 들어오면 그냥 리턴
        if not string:
            return completed_string
        
        # 균형잡힌 부분 체크
        left = 0
        right = 0
        point = 0
        
        for i, c in enumerate(string):
            if c == '(':
                left += 1
            else:
                right += 1
            if left == right:
                point = i + 1
                break
        
        # u와 v로 분리
        u = string[:point]
        v = string[point:]
        
        # u가 올바른 문자열이면
        if check_right(u):
            completed_string += u
            # 3-1
            if v:
                completed_string += check_string(v)
        # u가 올바른 문자열이 아니면
        else:
            completed_string = '('
            completed_string += check_string(v)
            completed_string += ')'
            
            u = u[1:-1]
            
            reversed_u = ''
            
            for p in u:
                if p == '(':
                    reversed_u += ')'
                else:
                    reversed_u += '('

            u = reversed_u
            completed_string += u
        
        return completed_string
    
    answer = check_string(p)
    
    return answer