m = int(input())

one_set = set()
one_set.add(1)

for _ in range(m):
  x, y = map(int, input().split())

  if x in one_set:
    one_set.pop()
    one_set.add(y)
  elif y in one_set:
    one_set.pop()
    one_set.add(x)
    
if one_set:
  print(one_set.pop())
else:
  print(-1)