n, s, m = map(int, input().split())
available_volumes = list(map(int, input().split()))

dp = [[False] * (m + 1) for _ in range(n + 1)]

dp[0][s] = True
for index, volume in enumerate(available_volumes):        
    for i, x in enumerate(dp[index]):
        if x:
            maximum = i + volume
            minimum = i - volume

            if maximum <= m:
                dp[index + 1][maximum] = True
            
            if minimum >= 0:
                dp[index + 1][minimum] = True

result = -1      

for i in range(m, -1, -1):
    if dp[n][i]:
        result = i
        break

print(result)