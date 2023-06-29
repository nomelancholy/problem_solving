scores = []

for i in range(1, 6):
  scores.append((sum(list(map(int, input().split()))), i))

scores.sort()
score, who = scores.pop()
print(who, score)