n, m = map(int, input().split())

for _ in range(n):
  s = input()
  for c in s[::-1]:
    print(c, end='')
  print()