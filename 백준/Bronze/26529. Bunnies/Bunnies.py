n = int(input())

dp = [1, 1, 2]

for _ in range(2, 46):
  dp.append(dp[-2] + dp[-1])

for _ in range(n):
  x = int(input())
  print(dp[x])