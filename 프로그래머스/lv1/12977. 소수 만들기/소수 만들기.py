from itertools import combinations



def solution(nums):
    # 모든 조합을 구해 합을 리스트로 만든다
    arr = list(combinations(nums, 3))
    
    numbers = []
    for comb in arr:
        numbers.append(sum(comb))    
    
    # 2부터 가장 큰 수 까지 수를 나열하고
    limit = max(numbers)
    sieve = set(range(2, limit + 1))
    
    # 2부터 가장 큰 수까지 순회하며 체 구성
    for i in range(2, limit + 1):
        if i in sieve:
            sieve -= set(range(2 * i, limit + 1, i))

    # 숫자가 체에 있으면 카운트 증가
    answer = 0
            
    for number in numbers:
        if number in sieve:
            answer += 1

    return answer