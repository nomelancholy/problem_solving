def solution(a, b):
    answer = 1
    
    check_list = []

    for i in range(min(a, b), 1, -1):
        if a % i == 0 and b % i == 0:
            a //= i
            b //= i
            
    while b != 1:
        for i in range(2, b + 1):
            if b % i == 0:
                check_list.append(i)
                b //= i
                break
        
    for n in check_list:
        if not (n == 2 or n == 5):
            answer = 2
            break
    
    return answer