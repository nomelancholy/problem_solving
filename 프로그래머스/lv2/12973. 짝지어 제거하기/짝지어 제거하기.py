from collections import deque

def solution(s):
    
    if len(s) < 2:
        return 0
    
    stack = []
    
    for c in list(s):
        if stack:
            if stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
        else:
            stack.append(c)
    
    if stack:
        return 0
    else:
        return 1