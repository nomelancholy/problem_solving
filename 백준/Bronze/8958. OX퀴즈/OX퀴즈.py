t = int(input())

for _ in range(t):
  n = input()
  score = 0
  point = 0
  for c in n:
    if c == 'O':
      point += 1
      score = score + point
    else:
      point = 0
  print(score)