import heapq

def solution(scoville, K):
    answer = 0
    
    heap = []
    # heap에 입력
    for s in scoville:
        heapq.heappush(heap, s)
        
    # min-heap의 root 노드가 k 미만일 동안은
    while heap[0] < K:
        # min-heap내에서 스코빌 지수가 가장 작은 값과 그 다음으로 작은 값을 확인하고
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        # 스코빌 지수를 섞는다
        mix_s = first + (second * 2)
        
        # 섞은 음식을 heap에 추가하고 횟수를 증가시킨다
        heapq.heappush(heap, mix_s)
        answer += 1
        
        # 만약 섞고 나서 음식이 하나만 남았고 그 하나가 K 미만이라면
        if len(heap) == 1 and heap[0] < K:
            # 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우이므로 answer를 -1로 만든다
            answer = -1
            break
        
    return answer