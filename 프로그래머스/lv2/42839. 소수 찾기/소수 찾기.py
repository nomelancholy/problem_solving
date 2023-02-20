from itertools import permutations
import math

def solution(numbers):
    
    candidates = []
    # 숫자를 쪼개
    crumbs = [n for n in numbers]
    
    # 순열 생성해서 리스트에 집어넣음
    for i in range(1, len(numbers) + 1):
        comb = list(permutations(crumbs, i))
        
        for c in comb:
            s = ''.join(c)
            s = s.lstrip('0')
            if s:
                candidates.append(int(s.lstrip('0')))
    
    # 중복 제거
    candidates = list(set(candidates))
        
    answer = 0
    
    for number in candidates:
        isPrime = True
        # 1 제외하고
        if number >= 2:
            # 소수인지 판별
            for i in range(2, int(math.sqrt(number)) + 1):
                if number % i == 0:
                    isPrime = False
                    break
            if isPrime:
                answer += 1
        
    return answer