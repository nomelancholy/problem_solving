def solution(number, limit, power):
    answer = 0
    
    knights = [i for i in range(1, number + 1)]

    powers = []
    
    for knight in knights:
        factors = set()
        for i in range(1, int(knight ** (1 / 2)) + 1):
            if knight % i == 0:
                factors.add(i)
                factors.add(knight // i)
                
        if len(factors) > limit:
            powers.append(power)
        else:
            powers.append(len(factors))
        
    answer = sum(powers)
    
    return answer