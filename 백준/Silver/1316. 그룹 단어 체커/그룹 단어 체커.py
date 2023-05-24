n = int(input())

answer = 0

for _ in range(n):
  
  word = input()
  used = set(word[0])
  before = word[0]
  flag = True
  
  for i in range(1, len(word)):
    if word[i] != before and word[i] in used:
      flag = False
      break
    before = word[i]
    used.add(word[i])

  if flag:
    answer += 1

print(answer)