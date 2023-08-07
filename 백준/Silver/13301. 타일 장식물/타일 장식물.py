n = int(input())

dp = [1, 1]

for _ in range(2, n):
  dp.append(dp[-1] + dp[-2])

if n == 1:
  print(4)
else:
  print((dp[-1] + (dp[-1] + dp[-2])) * 2)