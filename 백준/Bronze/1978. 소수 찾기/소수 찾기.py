n = int(input())
numbers = list(map(int, input().split()))

answer = 0

for number in numbers:
  if number == 1:
    continue
  flag = True
  for i in range(2, number):
    if number % i == 0:
      flag = False
      break
  if flag:
    answer += 1

print(answer)