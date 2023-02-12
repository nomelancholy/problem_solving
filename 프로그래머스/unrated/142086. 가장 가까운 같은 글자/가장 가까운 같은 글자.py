from collections import defaultdict

def solution(s):
    answer = []
    
    save_dict = defaultdict(int)
    
    for i, c in enumerate(s):
        if c in save_dict.keys():
            answer.append(i - save_dict[c])
        else:
            answer.append(-1)
        
        save_dict[c] = i
        
        
    return answer