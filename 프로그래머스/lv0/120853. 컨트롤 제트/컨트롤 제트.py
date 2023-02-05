def solution(s):
    answer = 0
    
    stack = []
    
    commands = s.split(' ')
    
    for c in commands:
        if c == 'Z':
            stack.pop()
        else:
            stack.append(int(c))
    
    answer = sum(stack)
    
    return answer