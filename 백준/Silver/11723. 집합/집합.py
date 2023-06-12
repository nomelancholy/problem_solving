import sys

m = int(sys.stdin.readline())

s = set()

for _ in range(m):
  commands = sys.stdin.readline().split()

  command = commands[0]

  if not (command == 'all' or command == 'empty'):
    number = int(commands[1])

  if command == 'add':
    if number not in s:
      s.add(number)
  elif command == 'remove':
    if number in s:
      s.remove(number)
  elif command == 'check':
    if number in s:
      print(1)
    else:
      print(0)
  elif command == 'toggle':
    if number in s:
      s.remove(number)
    else:
      s.add(number)
  elif command == 'all':
    s = set(i for i in range(1, 21))
  else:
    s = set()
  
  