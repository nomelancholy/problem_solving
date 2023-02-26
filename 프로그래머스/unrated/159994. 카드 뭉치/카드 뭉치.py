from collections import deque

def solution(cards1, cards2, goal):
    answer = ''
    
    c1 = deque(cards1)
    c2 = deque(cards2)
    
    g = deque(goal)
    
    while g:
        first = ''
        second = ''
        
        target = g.popleft()
        
        if c1:
            first = c1.popleft()
        if c2:
            second = c2.popleft()
            
        if target == first:
            c2.appendleft(second)
        elif target == second:
            c1.appendleft(first)
        else:
            g.appendleft(target)
            break
    
    if g:
        answer = 'No'
    else:
        answer = 'Yes'    
        
    return answer