def solution(n):
    answer = 0
    
    for i in range(1, 1000000):
        div, mod = divmod(n, i)
        if mod == 1:
            answer = i
            break
    return answer