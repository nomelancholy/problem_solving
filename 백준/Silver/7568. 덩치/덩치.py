n = int(input())

people = []

for i in range(n):
  x, y = map(int, input().split())
  people.append((x, y))

answer = [0] * n

for i in range(len(people)):
  x, y = people[i]
  rank = 1
  for j in range(len(people)):
    if i == j:
      continue

    p, q = people[j]

    if x < p and y < q:
      rank += 1
  
  answer[i] = rank

for r in answer:
  print(r, end=' ')