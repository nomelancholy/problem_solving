from collections import defaultdict

def solution(spell, dic):
    answer = 2
    
    for d in dic:
        if len(d) == len(spell):
            check_dict = defaultdict(int)
            for key in d:
                check_dict[key] += 1
            
            for s in spell:
                check_dict[s] -= 1
            
            if set(check_dict.values()) == {0}:
                answer = 1
                break
        
    return answer