def solution(arr, k):
    answer = []
    
    for n in arr:
        if n not in answer:
            answer.append(n)
        if len(answer) == k:
            break
    
    if len(answer) < k:
        for _ in range(k - len(answer)):
            answer.append(-1)
    
    return answer