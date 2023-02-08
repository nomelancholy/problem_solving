from collections import defaultdict

def solution(array):
    answer = 0
    
    check_dict = defaultdict(int)
    
    for number in array:
        check_dict[number] += 1
        
    max_count = max(check_dict.values())        
    
    answer_list = []
    
    for key, value in check_dict.items():
        if value == max_count:
            answer_list.append(key)
    
    if len(answer_list) > 1:
        answer = -1
    else:
        answer = answer_list[0]
    
    return answer