from math import gcd

x, y = map(int, input().split())

xy_gcd = gcd(x, y)

print(xy_gcd)
print(x * y // xy_gcd)