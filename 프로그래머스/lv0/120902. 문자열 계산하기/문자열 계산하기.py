from collections import deque

def solution(my_string):
    answer = 0
    
    operators = deque([])
    numbers = deque([])
    
    is_number = True
    
    number_str = ''
    for c in my_string:
        if c == ' ':
            if is_number:                
                numbers.append(int(number_str))
                number_str = ''
            is_number = not is_number
            continue
        if is_number:
            number_str += c
        else:
            operators.append(c)
    numbers.append(int(number_str))
    
    answer += numbers.popleft()
    
    while operators:
        operator = operators.popleft()
        number = numbers.popleft()
        
        if operator == '+':
            answer += number
        else:
            answer -= number
            
    return answer