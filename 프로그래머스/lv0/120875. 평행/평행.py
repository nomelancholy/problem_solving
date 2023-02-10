from itertools import combinations

def solution(dots):
    
    c = list(combinations(dots, 2))
    inclinations = []
    answer = 0
    
    for l, r in c:       
        inclination = (l[0] - r[0]) / (l[1] - r[1])
        
        if inclination in inclinations:
            answer = 1
            break
        else:
            inclinations.append(inclination)
        
    return answer