x_vertaxes = []
y_vertaxes = []

for _ in range(3):
  a, b = map(int, input().split())
  x_vertaxes.append(a)
  y_vertaxes.append(b)

print(min(x_vertaxes, key=x_vertaxes.count), end=' ')
print(min(y_vertaxes, key=y_vertaxes.count))