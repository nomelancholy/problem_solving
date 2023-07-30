k = int(input())

dp = [(1, 0), (0, 1)]

if k >= 2:
  for i in range(2, k + 1):
    a_cnt = dp[i-2][0] + dp[i-1][0]
    b_cnt = dp[i-2][1] + dp[i-1][1]
    dp.append((a_cnt, b_cnt))

a, b = dp[k]
print(a, b)