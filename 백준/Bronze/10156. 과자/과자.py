k, n, m = map(int, input().split())

answer = (k * n) - m

if answer < 0:
  answer = 0

print(answer)