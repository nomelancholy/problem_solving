n, m = map(int, input().split())

box = [0] * n

for _ in range(m):
  i, j , k = map(int, input().split())

  for index in range(i-1, j):
    box[index] = k

for ball in box:
  print(ball, end=' ')