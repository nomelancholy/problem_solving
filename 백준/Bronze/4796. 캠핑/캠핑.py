case_count = 0

while True:
  case_count += 1
  l, p, v = map(int, input().split())
  
  if l + p + v == 0:
    break
  
  div, mod = divmod(v, p)

  if mod < l:
    print(f'Case {case_count}: {div * l + mod}')
  else:
    print(f'Case {case_count}: {div * l + l}')