import sys
input = sys.stdin.readline

stack = list()

n = int(input())

for _ in range(n):
  commands = list(map(int, input().split()))
  if commands[0] == 1: 
    stack.append(commands[1])
  elif commands[0] == 2:
    if len(stack) > 0:
      print(stack.pop())
    else:
      print(-1)
  elif commands[0] == 3:
    print(len(stack))
  elif commands[0] == 4:
    if len(stack) > 0:
      print(0)
    else:
      print(1)
  elif commands[0] == 5:
    if len(stack) > 0:
      print(stack[-1])
    else:
      print(-1)