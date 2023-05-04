total = int(input())
type_count = int(input())

check_total = 0

for _ in range(type_count):
  cost, n = map(int, input().split())
  check_total += cost * n

if total == check_total:
  print('Yes')
else:
  print('No')