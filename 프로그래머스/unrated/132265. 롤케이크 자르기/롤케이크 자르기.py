from collections import Counter

def solution(topping):
    answer = 0
    topping_count = Counter(topping)
    check_set = set()
    
    while topping:
        t = topping.pop()
        check_set.add(t)
        topping_count[t] -= 1
        
        if topping_count[t] == 0:
            topping_count.pop(t)
        
        if len(check_set) == len(topping_count):
            answer += 1
    
    return answer