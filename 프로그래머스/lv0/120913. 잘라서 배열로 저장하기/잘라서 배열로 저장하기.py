def solution(my_str, n):
    answer = []
    
    index = 0
    
    for i in range (n, len(my_str) + 1, n):
        answer.append(my_str[index : i])
        index = i

    if len(my_str) % n != 0:
        answer.append(my_str[index:])
    
    return answer