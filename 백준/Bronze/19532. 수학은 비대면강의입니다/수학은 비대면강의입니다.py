a, b, c, d, e, f = map(int, input().split())

start = -999
is_end = False

for x in range(start, 1000):
  for y in range(start, 1000):
    if a * x + b * y == c:
      if d * x + e * y == f:
        print(x, end=' ')
        print(y)
        is_end = True
        break
  if is_end:
    break