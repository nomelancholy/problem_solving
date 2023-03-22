x = int(input())

dp = [0] * (x + 1)

for i in range(2, (x + 1)):
    # -1의 경우
    dp[i] = dp[i - 1] + 1
    # // 2의 경우
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[x])