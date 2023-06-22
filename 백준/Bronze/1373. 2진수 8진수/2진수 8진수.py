n = input()
answer = ''

for i in range(len(n), -1, -3):
  target = ''
  sum = 0
  if i - 3 >= 0:
    target = n[i-3: i]
  else:
    target = n[:i]
  if target:
    for j in range(len(target)):
      sum += int(target[j]) * (2 ** (len(target) - 1 - j))
    answer += str(sum)

print(answer[::-1])