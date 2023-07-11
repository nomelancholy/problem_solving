n = int(input())

schedules = []

for _ in range(n):
  start, end = map(int, input().split())
  schedules.append((start, end))

answer = 0
pre_start = 0

for start, end in sorted(schedules, key=lambda x:(-x[0], -x[1])):
  if pre_start == 0 or end <= pre_start:
    pre_start = start
    answer += 1

print(answer)