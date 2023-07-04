from collections import defaultdict

n = int(input())

numbers = []
number_dict = defaultdict(int)

for _ in range(n):
  i = int(input())
  numbers.append(i)
  number_dict[i] += 1

numbers.sort()

arr = sorted(number_dict.items(),  key=lambda x: (-x[1], x[0]))

third = 0

if len(arr) == 1:
  third = arr[0][0]
else:
  if arr[0][1] == arr[1][1]:
    third = arr[1][0]
  else:
    third = arr[0][0]

print(round(sum(numbers) / n))
print(numbers[n // 2])
print(third)
print(max(numbers) - min(numbers))