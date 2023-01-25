from itertools import permutations

def solution(numbers):
    answer = 0
    arr = list(permutations(numbers, 2))
    for a, b in arr:
        if a * b > answer:
            answer = a * b
    return answer