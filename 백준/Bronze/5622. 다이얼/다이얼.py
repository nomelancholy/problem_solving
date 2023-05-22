dials = ['', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

code = input()

answer = len(code)

for c in code:
  for index, dial in enumerate(dials):
    if c in dial:
      answer += (index + 1)

print(answer)