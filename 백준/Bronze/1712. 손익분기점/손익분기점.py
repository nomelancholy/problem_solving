a, b, c = map(int, input().split())

count = 0

if b >= c:
  print(-1)
else:
  print(a // (c - b) + 1)