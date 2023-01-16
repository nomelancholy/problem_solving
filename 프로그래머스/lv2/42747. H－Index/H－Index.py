def solution(citations):
    answer = 0
    
    citations.sort()
    
    counts = [0 for i in range(max(citations) + 1)]
    
    for c in citations:
        for i in range(c + 1):
            counts[i] += 1

    for index, count in enumerate(counts):
        if index <= count:
            answer = index
            
    return answer