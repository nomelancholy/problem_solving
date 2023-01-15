def solution(absolutes, signs):
    
    real = []
    
    for i, n in enumerate(absolutes):
        if not signs[i]:
            n *= -1
        real.append(n)
        
    answer = sum(real)
    
    return answer