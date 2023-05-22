def solution(my_string, m, c):
    answer = ''
    arr = []
    
    for i in range(len(my_string) // m):
        arr.append(my_string[:m])
        my_string = my_string[m:]
    
    for chunk in arr:
        answer += chunk[c - 1]
    
    return answer