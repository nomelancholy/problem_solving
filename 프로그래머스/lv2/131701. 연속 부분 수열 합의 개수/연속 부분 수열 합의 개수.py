from itertools import combinations

def solution(elements):
    answer = 0
    
    sum_set = set()
    
    sequence_parts = elements * 2
    
    for i in range(1, len(elements) + 1):
        for j in range(len(sequence_parts) - i):
            sum_set.add(sum(sequence_parts[j: j + i]))
    
    answer = len(sum_set)
    
    return answer