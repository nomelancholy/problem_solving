def solution(sides):
    answer = 0

    # 가장 긴 변의 길이 < 다른 두 변의 길이의 합
    # 가장 긴 변의 길이는 max(sides) 혹은 다른 하나일 수 있음     
    max_range = sum(sides) - 1
    min_range = max(sides) - min(sides) + 1
    
    answer = max_range - min_range + 1
    return answer