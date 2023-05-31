max_number = 0
max_index = 0

for i in range(1, 10):
  number = int(input())
  if number > max_number:
    max_number = number
    max_index = i

print(max_number)
print(max_index)