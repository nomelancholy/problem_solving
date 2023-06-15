numbers = list(map(int, input().split()))
answer = 0

check_number = min(numbers)

while True:
  count = 0
  for number in numbers:
    if check_number % number == 0:
      count += 1 
  if count >= 3:
    answer= check_number
    break

  check_number += 1

print(answer)