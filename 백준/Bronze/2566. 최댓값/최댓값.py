max_value = 0
max_coordinate = [0, 0]

for i in range(9):
  numbers = list(map(int, input().split()))
  for j in range(9):
    if numbers[j] > max_value:
      max_value = numbers[j]
      max_coordinate = [i, j]

print(max_value)

for point in max_coordinate:
  print(point + 1, end=' ')