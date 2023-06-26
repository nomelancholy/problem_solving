def get_n_number(n, base):
    convert_number = ''
    reference = '0123456789ABCDEF'
    
    if n == 0:
        return '0'
    
    while n:
        q, r = divmod(n, base)
        convert_number += reference[r]
        n = q
        
    return convert_number[::-1]
        

def solution(n, t, m, p):
    answer = ''
    full_string = ''
    
    target_number = 0
    
    while len(full_string) < t * m:
        result = get_n_number(target_number, n)
        full_string += str(result)
        target_number += 1
    
    index = p-1
    while len(answer) < t:
        answer += full_string[index]
        index += m
        
    return answer