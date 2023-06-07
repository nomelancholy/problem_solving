t = int(input())

for _ in range(t):
  h, w, n = map(int, input().split())
  div, mod = divmod(n, h)

  y = 0
  x = 1

  x += div
  
  if mod == 0:
    y = h
    x -= 1
  else:
    y = mod

  answer = ''

  answer += str(y)
  if len(str(x)) == 1:
    answer += '0' + str(x)
  else:
    answer += str(x)

  print(answer)
  
  