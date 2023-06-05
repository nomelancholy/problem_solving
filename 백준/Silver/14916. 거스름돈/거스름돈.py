n = int(input())

answer = -1

start = n // 5

for i in range(start, -1, -1):
  diff = n - (5 * i)

  if diff % 2 == 0:
    answer = i + diff // 2
    break

print(answer)