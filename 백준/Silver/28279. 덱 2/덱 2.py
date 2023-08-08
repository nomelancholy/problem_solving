from collections import deque
import sys

input = sys.stdin.readline

d = deque()

n = int(input())

for _ in range(n):
  commands = list(map(int, input().split()))
  if commands[0] == 1: 
    d.appendleft(commands[1])
  elif commands[0] == 2:
    d.append(commands[1])
  elif commands[0] == 3:
    if len(d) == 0:
      print(-1)
    else:
      print(d.popleft())
  elif commands[0] == 4:
    if len(d) == 0:
      print(-1)
    else:
      print(d.pop())
  elif commands[0] == 5:
    print(len(d))
  elif commands[0] == 6:
    if len(d) == 0:
      print(1)
    else:
      print(0)
  elif commands[0] == 7:
    if len(d) == 0:
      print(-1)
    else:
      print(d[0])
  elif commands[0] == 8:
    if len(d) == 0:
      print(-1)
    else:
      print(d[-1])