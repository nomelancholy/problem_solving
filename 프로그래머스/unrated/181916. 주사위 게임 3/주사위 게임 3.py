from collections import defaultdict

def solution(a, b, c, d):
    answer = 0
    
    numbers = [a, b, c, d]
    dice_dict = defaultdict(int)
    
    for number in numbers:
        dice_dict[number] += 1
        
    number_of_cases = len(dice_dict.items())
    
    if number_of_cases == 1:
        answer = 1111 * list(dice_dict.keys())[0]
    elif number_of_cases == 2:
        if 2 in dice_dict.values():
            p, q = dice_dict.keys()
            answer = (p + q) * abs(p - q)
        else:
            p = 0
            q = 0
            for key, count in dice_dict.items():
                if count == 3:
                    p = key
                else:
                    q = key
            answer = (10 * p + q) ** 2
    elif number_of_cases == 3:
        targets = [key for key, count in list(dice_dict.items()) if count == 1]
            
        a, b = targets
        answer = a * b
    else:
        answer = min(list(dice_dict.keys()))
        
    
    return answer