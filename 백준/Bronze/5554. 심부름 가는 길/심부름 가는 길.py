total_second = 0

for _ in range(4):
  total_second += int(input())

m, s = divmod(total_second, 60)

print(m)
print(s)