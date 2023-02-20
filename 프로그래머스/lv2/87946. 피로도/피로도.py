from itertools import permutations

def solution(k, dungeons):
    
    answer = -1
    
    # 순열을 만들고
    p_list = list(permutations(dungeons, len(dungeons)))
    
    # 순서대로 다 돌려본다
    for d_list in p_list:
        
        clear_count = 0
        player = k
        
        for d in d_list:
            # 던전 입장 가능하면 깬다
            if player >= d[0]:
                player -= d[1]
                clear_count += 1
            else:
                break
        
        answer = max(answer, clear_count)
    
    return answer