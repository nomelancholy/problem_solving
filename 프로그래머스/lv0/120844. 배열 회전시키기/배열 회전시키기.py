def solution(numbers, direction):
    answer = []
    
    if direction == 'left':
        n = numbers[0]
        numbers.append(n)
        answer = numbers[1:]
    else:
        n = numbers.pop()
        answer = [n, *numbers]
    
    return answer