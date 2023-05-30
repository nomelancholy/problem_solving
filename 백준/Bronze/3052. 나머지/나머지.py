answer_set = set()

for _ in range(10):
  answer_set.add(int(input()) % 42)

print(len(answer_set))