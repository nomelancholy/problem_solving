word = input()

if len(word) % 2 == 1:
  word = word[:len(word) // 2] + word[len(word) // 2 + 1:]

answer = 1

stack = []

for i, c in enumerate(word):
  if i < len(word) // 2:
    stack.append(c)
  else:
    p = stack.pop()
    if p != c:
      answer = 0
      break

print(answer)