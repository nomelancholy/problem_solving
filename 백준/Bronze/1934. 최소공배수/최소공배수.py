from math import gcd

t = int(input())

for _ in range(t):
  a, b = map(int, input().split())
  ab_gcd = gcd(a, b)
  print(a * b // ab_gcd)