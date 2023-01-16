from math import gcd

def solution(n, m):
    
    # 최대 공약수
    d = gcd(n ,m)
    # 최소 공배수
    lcm = n * m // d
    
    answer = [d, lcm]
    
    return answer