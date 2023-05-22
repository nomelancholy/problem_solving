counts = list(map(int, input().split()))
right_counts = [1, 1, 2, 2, 2, 8]

answers = []

for i  in range(6):
  if counts[i] == right_counts:
    answers.append(0)
  else:
    answers.append(right_counts[i] - counts[i])

for answer in answers:
  print(answer, end=' ')