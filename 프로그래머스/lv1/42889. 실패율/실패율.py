from collections import defaultdict

def solution(N, stages):
    
    # 스테이지 클리어 현황 저장
    clear_status = [0] * (N + 1)
    # 도전중인 스테이지 기록 저장
    challenging_stage = [0] * (N + 1)
    
    # 실패율 계산 dict
    failure_rate = defaultdict(int)
    
    # 클리어한 내역을 저장하고 도전중인 스테이지 기록
    for stage in stages:
        for i in range(1, stage + 1):
            if i <= N:
                clear_status[i] += 1
        if stage <= N:
            challenging_stage[stage] += 1
    
    # 실패율을 계산해 저장한다.
    for i in range(1, N + 1):
        if clear_status[i] == 0:
            failure_rate[i] = 0
        else:
            failure_rate[i] = challenging_stage[i] / clear_status[i]
    
    # 실패율로 정렬해
    sorted_rate = sorted(failure_rate.items(), key = lambda i:i[1], reverse = True)
    
    print(sorted_rate)
    
    # 키 값만 담는다
    answer = [k for k, v in sorted_rate]

    return answer