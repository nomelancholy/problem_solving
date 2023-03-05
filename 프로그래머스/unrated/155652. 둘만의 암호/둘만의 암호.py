def solution(s, skip, index):
    answer = ''
    
    skip_list = [c for c in skip]
    
    for c in s:
        for i in range(index):
            c = chr(ord(c) + 1)
            if not c.isalpha():
                c = 'a'
            while c in skip_list:
                c = chr(ord(c) + 1)
                if not c.isalpha():
                    c = 'a'
                
        answer += c    
        
    return answer