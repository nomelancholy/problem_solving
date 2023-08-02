n = int(input())

for _ in range(n):
  s = input()
  new_s = ''
  for c in s:
    new_s += c.lower()

  print(new_s)