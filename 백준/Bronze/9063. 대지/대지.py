n = int(input())

x_set = set()
y_set = set()

for _ in range(n):
  x, y = map(int, input().split())
  x_set.add(x)
  y_set.add(y)

min_x = min(x_set)
max_x = max(x_set)
min_y = min(y_set)
max_y = max(y_set)

if min_x == max_x or min_y == max_x:
  print(0)
else:
  print((max_x - min_x) * (max_y - min_y))