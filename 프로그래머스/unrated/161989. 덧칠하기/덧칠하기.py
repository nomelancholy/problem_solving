def solution(n, m, section):
    answer = 0
    
    sides = [i for i in range(1, n + 1)]
    side_set = set(sides) - set(section)
    
    for side in section:
        if side in side_set:
            continue
        answer += 1
        for i in range(side, side + m):
            side_set.add(i)
    
    return answer