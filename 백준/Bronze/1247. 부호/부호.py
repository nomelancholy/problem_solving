for _ in range(3):
  n = int(input())
  s = 0
  for _ in range(n):
    s += int(input())

  if s == 0:
    print('0')
  elif s > 0:
    print('+')
  elif s < 0:
    print('-')