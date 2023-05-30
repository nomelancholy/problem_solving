n = int(input())

for i in range(n):
  for j in range(n):
    if n - j <= i + 1:
      print('*', end="")
    else:
      print(" ", end="")
  print("")