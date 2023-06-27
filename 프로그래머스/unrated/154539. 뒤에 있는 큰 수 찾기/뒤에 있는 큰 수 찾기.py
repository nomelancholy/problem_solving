

def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    
    for i in range(len(numbers)):
        if stack != []:
            
            while stack != [] and stack[-1][1] < numbers[i]:
                target_index, target_number = stack.pop()
                answer[target_index] = numbers[i]
        stack.append((i, numbers[i]))
    
    return answer