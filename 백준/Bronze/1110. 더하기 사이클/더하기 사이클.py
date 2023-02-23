init_number_str = input()
init_number = int(init_number_str)

count = 0
is_first = True

number = init_number

while is_first or number != init_number:
    is_first = False
    
    # 십의 자리 숫자
    decimal_number = number // 10
    # 일의 자리 숫자
    digit_number = number % 10

    new_number = decimal_number + digit_number
    
    number = (digit_number * 10) + (new_number % 10)

    count += 1

print(count)