import math

def solution(n, k):
    answer = 0
    
    if n == 1:
        return 0
    
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)

    rev_base = rev_base[::-1] 
    
    split_base = rev_base.split('0')
    numbers = []
    
    for c in split_base:
        if c:
            numbers.append(int(c))
    
    for number in numbers:
        if number == 1:
            continue
        flag = True
        for i in range(2, int(math.sqrt(number) + 1)):
            if number % i == 0:
                flag = False
                break
        if flag:
            answer += 1
    
    return answer