from collections import deque

n = int(input())
numbers = list(map(int, input().split()))

balloons = deque()

for idx, number in enumerate(numbers):
  balloons.append((idx + 1, number))


answer = []

while len(balloons) > 0:
  index, number = balloons.popleft()
  answer.append(index)

  if len(balloons) == 0:
    break

  if number > 0:
    for _ in range(number-1):
      balloons.append(balloons.popleft())  
  else:
    for _ in range(abs(number)):
      balloons.appendleft(balloons.pop())
  
for i in answer:
   print(i, end=' ')