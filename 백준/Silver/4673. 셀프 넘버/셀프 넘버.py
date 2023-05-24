not_self_number = []

for i in range(1, 10001):
  number = i 
  for c in str(i):
    number += int(c)
  not_self_number.append(number)

for i in range(1, 10001):
  if i not in not_self_number:
    print(i)