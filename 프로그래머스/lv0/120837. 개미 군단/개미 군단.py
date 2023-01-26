def solution(hp):
    answer = 0
    
    attacks = [5, 3, 1]

    while hp != 0:
        for attack in attacks:
            v, r = divmod(hp, attack)
            answer += v
            hp = r
    
    return answer