n = int(input())

students = list(map(int, input().split()))

now = 0
stack = []

for student in students:
  if student == now + 1:
    now += 1
  elif stack and stack[-1] == now + 1:
    while stack and stack[-1] == now + 1:
      stack.pop()
      now += 1
    stack.append(student)
  else:
    stack.append(student)

while stack:
  if stack.pop() == now + 1:
    now += 1
  else:
    break

if stack:
  print('Sad')
else:
  print('Nice')