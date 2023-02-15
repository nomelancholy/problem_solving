from collections import defaultdict

def solution(id_list, report, k):
    
    # 신고 현황
    report_status = defaultdict(list)
    # 신고당한 횟수
    reported_count = defaultdict(int)
    
    # 초기화
    for id in id_list:
        report_status[id] = []
        reported_count[id] = 0
        
    # 중복 신고 제거
    report = list(set(report))
    
    # 신고 현황과 횟수 저장
    for detail in report:
        reporter, victim = detail.split()
        
        report_status[reporter].append(victim)
        reported_count[victim] += 1
    
    # 이용 정지된 유저 확인
    stopped_user = [id for id, count in reported_count.items() if count >= k]
    
    # 정답 배열 초기화
    answer = [0] * len(id_list)
    
    # 이용 정지된 유저 목록을 순회하면서
    for user in stopped_user:
        # 신고 현황을 보고
        for index, status in enumerate(report_status.items()):
            reporter, victim = status
            
            # 정지된 유저를 신고한 유저에 해당하는 배열 카운트 + 1
            if user in victim:
                answer[index] += 1
            
    return answer