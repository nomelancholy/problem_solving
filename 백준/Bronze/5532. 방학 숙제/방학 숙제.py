l = int(input())

a = int(input())
b = int(input())
c = int(input())
d = int(input())

days = 0

while a > 0 or b > 0:
  days += 1

  a -= c
  b -= d

print(l - days)