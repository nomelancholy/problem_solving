def solution(k, score):
    answer = []
    
    hall_of_honor = []
    
    for s in score:
        if len(hall_of_honor) < k:
            hall_of_honor.append(s)
        else:
            if min(hall_of_honor) < s:
                hall_of_honor = hall_of_honor[1:] + [s]
            
        hall_of_honor.sort()
        answer.append(min(hall_of_honor))
        
        
    return answer