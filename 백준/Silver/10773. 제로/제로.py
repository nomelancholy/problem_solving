k = int(input())

stack = []

for _ in range(k):
  i = int(input())
  if i == 0:
    if stack:
      stack.pop()
  else:
    stack.append(i)

print(sum(stack))