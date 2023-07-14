import math

a, i = map(int, input().split())
start = a * i

while i == math.ceil(start / a):
  start -= 1

print(start + 1)
