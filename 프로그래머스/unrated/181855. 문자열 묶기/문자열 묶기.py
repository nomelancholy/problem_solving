from collections import defaultdict

def solution(strArr):
    answer = 0
    
    len_dict = defaultdict(list)
    
    for string in strArr:
        len_dict[len(string)].append(string)
        
    for arr in list(len_dict.values()):
        answer = max(answer, len(arr))
        
    return answer