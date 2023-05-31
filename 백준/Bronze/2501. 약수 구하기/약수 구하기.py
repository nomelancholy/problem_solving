n, k = map(int, input().split())

flag = False
count = 0

for i in range(1, n + 1):
  if n % i == 0:
    count += 1
  
  if count == k:
    flag = True
    print(i)
    break

if not flag:
  print(0)