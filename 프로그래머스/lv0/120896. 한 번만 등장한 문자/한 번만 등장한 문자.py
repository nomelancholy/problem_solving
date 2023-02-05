from collections import defaultdict

def solution(s):
    
    check_dict = defaultdict(int)
    
    answer = ''
    
    for c in s:
        check_dict[c] += 1
        
    for key, value in check_dict.items():
        if value == 1:
            answer += key
    
    answer = ''.join(sorted(answer))
    
    return answer