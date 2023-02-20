def solution(land):
    answer = 0
    
    visited = [[0] * 4 for _ in range(len(land))]
    
    # 첫 줄 기록
    for i in range(4):
        visited[0][i] = land[0][i]
        
    # 두번째 행부터 가는데
    for i in range(1, len(land)):
        # 각 열 돌면서
        for j in range(4):
            # 이전 4열과 모두 비교하는데
            for k in range(4):
                # 연속된 열 말고는
                if j == k:
                    continue
                # 이전 행의 최고 점수 값 + 현재 열 값 더해서
                new_score = visited[i-1][k] + land[i][j]
                # 지금있는 값과 대소 비교
                visited[i][j] = max(visited[i][j], new_score)

    answer = max(visited[len(land) - 1])

    return answer