n, b = input().split()
b = int(b)

answer = 0

for i, c in enumerate(n[::-1]):
  t = 0
  if c.isalpha():
    t = int(ord(c)) - 55
  else:
    t = int(c)

  answer += t * (b ** i)

print(answer)