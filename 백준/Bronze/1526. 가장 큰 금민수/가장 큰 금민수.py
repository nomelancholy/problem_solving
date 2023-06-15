n = int(input())

answer = 4

for i in range(n, 3, -1):
  flag = True
  for c in str(i):
    if not (c == '4' or c == '7'):
      flag = False
      break
  if flag:
    answer = i
    break

print(answer)