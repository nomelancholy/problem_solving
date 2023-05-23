def solution(arr, queries):
    answer = []
    
    for query in queries:
        s, e, k = query
        
        targets = [n for n in arr[s:e + 1] if n > k]
        
        if targets:
            answer.append(min(targets))
        else:
            answer.append(-1)
    
    return answer