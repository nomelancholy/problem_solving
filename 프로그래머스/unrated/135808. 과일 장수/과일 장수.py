import heapq

def solution(k, m, score):
    answer = 0
    
    heap = []
    
    for s in score:
        heapq.heappush(heap, -s)
    
    while len(heap) >= m:
        box = []
        for _ in range(m):
            box.append(-heapq.heappop(heap))
        
        answer += m * min(box)
    
    return answer