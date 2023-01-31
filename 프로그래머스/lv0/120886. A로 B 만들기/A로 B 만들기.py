from collections import defaultdict

def solution(before, after):
    answer = 0
    
    check_dict = defaultdict(int)
    
    for c in before:
        check_dict[c] += 1
        
    for c in after:
        check_dict[c] -= 1
        
    result = set(check_dict.values())
    
    if result == {0}:
        answer = 1
    
    return answer