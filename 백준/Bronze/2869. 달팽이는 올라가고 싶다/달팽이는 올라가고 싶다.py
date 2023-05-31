a, b, v = map(int, input().split())

if a == v:
  print(1)
else:
  v -= b

  div, mod = divmod(v, a-b)
  if mod == 0:
    print(div)
  else:
    print(div + 1)