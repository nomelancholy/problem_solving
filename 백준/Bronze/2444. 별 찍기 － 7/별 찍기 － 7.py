n = int(input())
n -= 1

for i in range(2 * n + 1):
  for j in range(2 * n + 1):
    if i <= n:
      if j >= n - i and j <= n + i:
        print('*', end='')
      else:
        if j > n:
          continue
        else:
          print(' ', end='')
    else:
      if j >= i - n and j <= n * 2 - (i - n):
        print('*', end='')
      else:
        if j > n:
          continue
        print(' ', end='')
  print('')