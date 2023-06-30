from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

d = deque([])

for _ in range(n):
  commands = list(input().split())

  if commands[0] == 'push_back':
    d.append(commands[1])
  elif commands[0] == 'push_front':
    d.appendleft(commands[1])
  elif commands[0] == 'pop_front':
    if d:
      number = d.popleft()
      print(number)
    else:
      print(-1)
  elif commands[0] == 'pop_back':
    if d:
      number = d.pop()
      print(number)
    else:
      print(-1)
  elif commands[0] == 'size':
    print(len(d))
  elif commands[0] == 'empty':
    if len(d) == 0:
      print(1)
    else:
      print(0)
  elif commands[0] == 'front':
    if d:
      print(d[0])
    else:
      print(-1)
  elif commands[0] == 'back':
    if d:
      print(d[-1])
    else:
      print(-1)
