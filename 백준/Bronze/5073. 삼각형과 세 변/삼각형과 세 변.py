while True:
  lines = list(map(int, input().split()))
  lines.sort()
  if lines[0] == 0 and lines[1] == 0 and lines[2] == 0:
    break
  if lines[-1] >= sum(lines[:2]):
    print('Invalid')
  else:
    line_kinds = len(set(lines))
    if line_kinds == 3:
      print('Scalene')
    elif line_kinds == 2:
      print('Isosceles')
    elif line_kinds == 1:
        print('Equilateral')