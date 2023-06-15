from collections import defaultdict

n = int(input())

student_dict = defaultdict(set)

records = []

for _ in range(n):
  records.append(list(map(int, input().split())))

for r in range(n):
  for c in range(5):
    student_class = records[r][c]
    for r2 in range(r + 1, n):
      if student_class == records[r2][c]:
        student_dict[r + 1].add(r2 + 1)
        student_dict[r2 + 1].add(r + 1)

answer = 1

if student_dict:

  count_dict = {k: len(v) for k, v in student_dict.items()}
  
  answer = max(count_dict, key=count_dict.get)

print(answer)