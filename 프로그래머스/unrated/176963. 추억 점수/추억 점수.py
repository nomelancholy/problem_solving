def solution(name, yearning, photo):
    answer = []
    
    name_yearning_pair = dict(zip(name, yearning))
    
    for names in photo:
        count = 0
        for name in names:
            if name in name_yearning_pair:
                count += name_yearning_pair[name]
        answer.append(count)
        
    return answer