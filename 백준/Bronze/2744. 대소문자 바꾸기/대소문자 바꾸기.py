n = input()

answer = ''

for c in n:
  if c.isupper():
    answer += c.lower()
  else:
    answer += c.upper()

print(answer)