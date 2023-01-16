def solution(brown, yellow):
    answer = []
    
    possibles = []
    
    half = brown // 2
    
    for i in range(1, half + 1):
        # 테두리 토대로 크기 유추
        x = half - i
        y = i + 2
        if x >= y:
            possibles.append([half - i, i + 2])
        else:
            # 가로 길이는 세로 길이와 같거나 길다
            break
    
    # 갯수로 체크
    for x, y in possibles:
        if brown + yellow == x * y:
            answer = [x, y]
            break
    
    return answer