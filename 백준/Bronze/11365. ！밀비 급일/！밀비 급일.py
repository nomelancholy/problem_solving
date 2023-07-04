while True:
  s = input()
  if s == 'END':
    break
  for c in s[::-1]:
    print(c, end='')
  print()