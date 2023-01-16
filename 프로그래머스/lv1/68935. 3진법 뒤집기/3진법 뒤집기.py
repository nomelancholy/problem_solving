def solution(n):
    answer = 0
    
    # 진법 변환
    reverse_three = ''

    while n != 0:
        div, mod = divmod(n, 3)
        reverse_three += str(mod)
        n = div
        
    answer = int(reverse_three, 3)
    
    return answer