n = int(input())

root = 2

for i in range(1, n + 1):
  root += 2 ** (i - 1)  

print(root ** 2)