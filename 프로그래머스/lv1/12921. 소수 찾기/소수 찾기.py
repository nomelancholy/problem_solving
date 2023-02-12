import math

# 소수 확인 함수 (기존에 풀었던 방식)
def is_prime(x):
    # 2부터 자신의 제곱근까지 반복하면서
    for i in range(2, int(math.sqrt(x)) + 1):
        # 나누어 떨어지는 수가 있으면 소수가 아니고
        if x % i == 0:
            return False
    # 없으면 소수다
    return True
    

def solution(n):
    # 2부터 구하려는 수까지 나열한다
    sieve = set(range(2, n + 1))
    # 2부터 구하려는 수까지 순회하며
    for i in range(2, n + 1):
        # 수가 체에 있으면
        if i in sieve:
            # 그 수를 제외한 그 수의 배수들을 체에서 지운다
            sieve -= set(range(2 * i, n + 1, i))
    
    # 체에는 소수만 남아있다
    return len(sieve)