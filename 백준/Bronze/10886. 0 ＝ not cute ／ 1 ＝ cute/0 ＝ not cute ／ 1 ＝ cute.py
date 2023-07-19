n = int(input())

result = [0, 0]

for _ in range(n):
  result[int(input())] += 1

if result[0] > result[1]:
  print('Junhee is not cute!')
else:
  print('Junhee is cute!')