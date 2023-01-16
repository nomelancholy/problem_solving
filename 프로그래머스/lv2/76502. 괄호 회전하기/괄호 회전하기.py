from collections import deque

def solution(s):
    
    if len(s) < 2:
        return 0
    
    answer = 0
    
    rotate_count = 0
    
    q = deque(list(s))

    def isRight(q):
        stack = []
        
        for c in q:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            elif c == ')':
                if stack:
                    top = stack.pop()
                    if top != '(':
                        return False
                else:
                    return False
            elif c == '}':
                if stack:
                    top = stack.pop()
                    if top != '{':
                        return False
                else:
                    return False
            elif c == ']':
                if stack:
                    top = stack.pop()
                    if top != '[':
                        return False
                else:
                    return False
                
        if stack:
            return False
        else:    
            return True
    
    while rotate_count != len(s) - 1:        
        if isRight(q):
            answer += 1
            
        head = q.popleft()
        q.append(head)
        
        rotate_count += 1
    
    return answer