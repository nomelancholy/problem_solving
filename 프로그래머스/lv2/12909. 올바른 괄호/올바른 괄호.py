def solution(s):
    
    stack = []
    
    for c in s:
        if c == '(':
            stack.append(c)
        else:
            if stack:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            else:
                return False
                    
    if stack:
        return False
    else:
        return True