numbers = list(map(int, input().split()))

answer = 0

for number in numbers:
  answer += number ** 2

answer %= 10

print(answer)