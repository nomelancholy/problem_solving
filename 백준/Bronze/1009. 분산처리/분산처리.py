t = int(input())

for _ in range(t):
  a, b = map(int, input().split())
  
  answer = pow(a, b, 10)

  if answer == 0:
    answer = 10
  
  print(answer)