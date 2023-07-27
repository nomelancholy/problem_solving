n = int(input())

score = 0
total = 0

answers = list(map(int, input().split()))

for answer in answers:
  if answer == 0:
    score = 0
  else:
    score += 1
  total += score

print(total)