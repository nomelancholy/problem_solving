s = int(input())

now = 0
num_range = 2

while now < s:
  now += num_range
  num_range += 1

print(num_range - 2)