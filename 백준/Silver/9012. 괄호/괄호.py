t = int(input())

for _ in range(t):
  pairs = list(input())
  stack = []
  is_break = False
  for pair in pairs:
    if pair == '(':
      stack.append(pair)
    else:
      if not stack:
        is_break = True
        break
      stack.pop()
  if is_break:
    print('NO')
    continue
  if stack:
    print('NO')
  else:
    print('YES')