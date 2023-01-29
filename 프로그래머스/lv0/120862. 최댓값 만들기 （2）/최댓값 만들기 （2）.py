from itertools import combinations

def solution(numbers):
    answer = -100000000
    
    combs = list(combinations(numbers, 2))
    
    for a, b in combs:
        if a * b > answer:
            answer = a * b
    
    return answer