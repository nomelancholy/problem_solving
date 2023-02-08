def solution(polynomial):
    
    answer = ''
    
    commands = polynomial.split(' ')

    constant_number = 0
    x_number = 0
    
    for command in commands:
        if command == '+':
            continue
        if command.isdigit():
            constant_number += int(command)
        else:
            if len(command) == 1:
                x_number += 1
            else:
                x_number += int(command[:-1])
    
    if x_number == 0:
        if constant_number == 0:
            answer = '0'
        else:
            answer = str(constant_number)
    else:
        if x_number == 1:
            answer = 'x'
        else:
            answer = f'{x_number}x'
        
        if constant_number != 0:
            answer += f' + {constant_number}'
    
    return answer