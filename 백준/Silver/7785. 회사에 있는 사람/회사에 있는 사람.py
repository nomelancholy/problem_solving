from collections import defaultdict

n = int(input())

attendance_dict = defaultdict(bool)

for _ in range(n):
  name, status = input().split()

  if status == 'enter':
    attendance_dict[name] = True
  else:
    attendance_dict[name] = False

on_list = [name for name, status in attendance_dict.items() if status]

on_list.sort(reverse=True)

for name in on_list:
  print(name)