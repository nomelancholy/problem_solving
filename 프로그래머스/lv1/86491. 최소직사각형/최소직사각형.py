def solution(sizes):

    # 가장 큰 수
    x = 0
    # 작은 값 중 가장 큰 수
    y = 0
    
    for size in sizes:
        # 가장 큰 수
        if x < max(size):
            x = max(size)
        # 작은 값 중 가장 큰 수
        if y < min(size):
            y = min(size)
        
    answer = x * y
    return answer