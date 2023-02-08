import math

def solution(common):
    answer = 0

    if common[-1] - common[-2] == common[-2] - common[-3]:
        # 등차 수열
        answer = common[-1] + (common[-1] - common[-2])
    else:
        # 등비 수열
        rate = common[-1] // common[-2]
        
        if common[-1] < 0:
            answer = common[-1] * -rate
        elif common[-1] == 0:
            answer = -common[-2]
        else:
            answer = common[-1] * rate
    
    return answer