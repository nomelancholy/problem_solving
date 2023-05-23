def solution(my_string, queries):
    answer = ''
    
    temp_list = list(my_string)
    
    for s, e in queries:
        
        temp_list = temp_list[:s] + list(reversed(temp_list[s : e + 1])) + temp_list[e + 1:]
    
    answer = ''.join(temp_list)
    
    return answer