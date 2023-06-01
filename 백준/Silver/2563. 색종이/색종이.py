n = int(input())

arr = [[0 for j in range(100)] for i in range(100)]

for _ in range(n):
  left, bottom = map(int, input().split())

  for i in range(left, left + 10):
    for j in range(bottom, bottom + 10):
      arr[i][j] = 1

answer = 0

for i in range(100):
  for j in range(100):
    if arr[i][j] == 1:
      answer += 1

print(answer)