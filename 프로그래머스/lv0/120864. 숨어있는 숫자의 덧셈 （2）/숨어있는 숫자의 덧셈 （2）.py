def solution(my_string):
    answer = 0
    number_str = ''
    
    for c in my_string:
        if c.isdigit():
            number_str += c
        else:
            if number_str:
                answer += int(number_str)
                number_str = ''
    
    if number_str:
        answer += int(number_str)
    
    return answer