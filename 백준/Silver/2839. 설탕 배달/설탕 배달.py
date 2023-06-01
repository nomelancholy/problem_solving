n = int(input())

answer = 5000
start = n // 5

if start == 0:
  if n == 3:
    answer = 1
  else:
    answer = -1
else:
  for i in range(start, -1, -1):
    div, mod = divmod(n - (5 * i), 3)
    if mod == 0:
      bags = i + div
      
      answer = min(answer, bags)

if answer == 5000:
  print(-1)
else:
  print(answer)