def solution(numbers):
    answer = 0
    
    answer_string = ''
    
    check_dict = {'zero': '0', 'one': '1', 'two' : '2', 'three' : '3', 'four' : '4', 'five' : '5', 'six' : '6', 'seven' : '7', 'eight' : '8', 'nine' : '9'}
    
    
    while numbers:
        for key, value in check_dict.items():
            if numbers.startswith(key):
                answer_string += value
                numbers = numbers[len(key):]
    
    answer = int(answer_string)
    
    return answer