def solution(s):
    answer = 0
    
    target = ''
    target_cnt = 0
    other_cnt = 0
    
    for c in s:
        if target == '':
            target = c
            target_cnt += 1
            continue
        if target == c:
            target_cnt += 1
        else:
            other_cnt += 1
            
        if target_cnt == other_cnt:
            answer += 1
            target = ''
            target_cnt = 0
            other_cnt = 0
        
    if target:
        answer += 1
    
    return answer