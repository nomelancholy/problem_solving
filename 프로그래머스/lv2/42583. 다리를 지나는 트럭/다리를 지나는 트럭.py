from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    time = 0
    
    # 트럭 큐 생성
    truck_q = deque(truck_weights)
    # 다리도 큐
    bridge_q = deque([])
    
    # 진행 상황 리스트
    progress = []
    progress_index = 0
    
    # 1초에 1씩 이동
    while truck_q or bridge_q:
        # 지금 다리 무게에 여유가 있다면
        if weight >= sum(bridge_q):
            # 남은 트럭이 있는지, 그리고 그걸 더해도 다리 무게에 여유가 있는지 확인해서
            if truck_q and weight >= sum(bridge_q) + truck_q[0]:
                # 트럭 추가하고
                t = truck_q.popleft()
                bridge_q.append(t)
                # 그 트럭의 진행 상황을 기록하자
                progress.append(bridge_length)
                
        # 하나씩 진행 상황 감소
        for i in range(progress_index, len(progress)):
            progress[i] -= 1
            # 끝에 도달한 트럭이 있으면 다리에서 빼고 진행 상황도 그만 기록한다
            if progress[i] == 0:
                bridge_q.popleft()
                progress_index += 1
                
        # 여기까지 1초 증가
        time += 1                
    
    # 마지막 지나는 순간 기록해서 리턴
    answer = time + 1
    
    return answer