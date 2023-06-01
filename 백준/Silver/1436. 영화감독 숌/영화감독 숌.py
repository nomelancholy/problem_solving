n = int(input())
count = 0
number = 665

while True:
  number += 1

  if '666' in str(number):
    count += 1

  if count == n:
    break

print(number)