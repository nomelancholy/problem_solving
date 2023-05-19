students = [i for i in range(1, 31)]

for _ in range(28):
  students.remove(int(input()))

for no_enter in students:
  print(no_enter)