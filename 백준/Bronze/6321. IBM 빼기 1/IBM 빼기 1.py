n = int(input())

for i in range(n):
  print(f'String #{i + 1}')
  s = input()
  answer = ''
  
  for c in s:
    next = ord(c) + 1
    if next == 91:
      answer += 'A'
    else:
      answer += chr(next)

  print(answer)
  if i != n - 1:
    print()