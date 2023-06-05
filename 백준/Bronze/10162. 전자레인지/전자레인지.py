t = int(input())

times = [300, 60, 10]

answer = []

for time in times:
  div, mod = divmod(t, time)
  answer.append(div)
  t = mod

if t == 0:
  for count in answer:
    print(count, end=' ')
else:
  print(-1)