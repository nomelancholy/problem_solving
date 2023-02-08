def solution(num, total):
    answer = []
    
    candidates = [i for i in range(-total - num, total + num)]
    
    for i, _ in enumerate(candidates):
        if total == sum(candidates[i : i + num]):
            answer = candidates[i : i + num]
            break
    
    return answer