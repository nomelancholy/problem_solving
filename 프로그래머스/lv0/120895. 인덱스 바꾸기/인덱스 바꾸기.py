def solution(my_string, num1, num2):
    answer = ''
    
    pre = my_string[num1]
    post = my_string[num2]
    
    answer = my_string[:num1] + post + my_string[num1 + 1: num2] + pre + my_string[num2 + 1:]
    
    return answer