t = int(input())

numbers = []

for _ in range(t):
  numbers.append(int(input()))

n = max(numbers)
dp = []

dp.append((1, 0))
dp.append((0, 1))

if n >= 2:
  for i in range(2, n + 1):
    z1, o1 = dp[i - 2]
    z2, o2 = dp[i - 1]

    dp.append((z1 + z2, o1 + o2))

for number in numbers:
  z, o = dp[number] 
  print(z, end=' ')
  print(o)