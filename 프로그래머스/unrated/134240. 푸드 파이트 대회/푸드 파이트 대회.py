from collections import deque

def solution(food):
    answer = ''
    
    left = deque([])
    right = deque([])
    
    for i, nth_food in enumerate(food):
        count = nth_food // 2
        
        for _ in range(count):
            left.append(str(i))
            right.appendleft(str(i))
    
    answer = ''.join(left) + '0' + ''.join(right)
    
    return answer