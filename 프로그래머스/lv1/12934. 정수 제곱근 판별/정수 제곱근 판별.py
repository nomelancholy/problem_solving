from math import sqrt

def solution(n):
    
    root = sqrt(n)
    answer = (int(root) + 1) ** 2 if root.is_integer() else -1

    return answer