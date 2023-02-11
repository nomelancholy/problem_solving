def solution(t, p):
    answer = 0
    
    for i in range(0, len(t) - len(p) + 1):
        target_number = int(t[i:i + len(p)])
        if target_number <= int(p):
            answer += 1
        
    return answer