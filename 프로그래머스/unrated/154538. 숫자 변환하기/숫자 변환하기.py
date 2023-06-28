def solution(x, y, n):
    if x == y:
        return 0

    dp = [int(1e9)] * (y + 1)
    dp[x] = 0

    for i in range(x, y + 1):
        if dp[i] == int(1e9):
            continue

        if i + n <= y:
            dp[i + n] = min(dp[i + n], dp[i] + 1)

        if i * 2 <= y:
            dp[i * 2] = min(dp[i * 2], dp[i] + 1)

        if i * 3 <= y:
            dp[i * 3] = min(dp[i * 3], dp[i] + 1)

    if dp[y] == int(1e9):
        return -1

    return dp[y]