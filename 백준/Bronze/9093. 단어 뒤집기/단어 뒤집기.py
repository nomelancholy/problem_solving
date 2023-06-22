t = int(input())

for _ in range(t):
  strings = input().split()
  for s in strings:
    print(s[::-1],end=' ')
  print()