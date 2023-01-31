from collections import defaultdict

def solution(my_string):
    answer = ''
    
    c_dict = defaultdict(int)
    
    for c in my_string:
        if c_dict[c]:
            pass
        else:
            c_dict[c] += 1
            answer += c
    
    return answer