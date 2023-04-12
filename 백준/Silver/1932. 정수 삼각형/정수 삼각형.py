n = int(input())

triangle = []

memo = [[0] * i for i in range(1, n + 1)]

for _ in range(n):
    triangle.append(list(map(int, input().split())))
    
# 첫 값 저장
memo[0][0] = triangle[0][0]

# 두번째 줄부터
for i in range(len(triangle) - 1):
    # 원소들을 각각 도는데
    for j in range(len(triangle[i])):
        # 왼쪽 대각선
        memo[i + 1][j] = max(memo[i + 1][j], memo[i][j] + triangle[i + 1][j])
        # 오른쪽 대각선
        memo[i + 1][j + 1] = max(memo[i + 1][j + 1], memo[i][j] + triangle[i + 1][j + 1])
        
print(max(memo[len(memo) - 1]))         