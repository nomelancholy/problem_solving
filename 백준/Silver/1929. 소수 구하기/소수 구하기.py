m, n = map(int, input().split())

number_set = set(range(1, n + 1))

for i in range(2, n + 1):
  if i in number_set:
    twotimes_number_set = set(range(2 * i, n + 1, i))
    number_set -= twotimes_number_set
    
for i in number_set:
  if i == 1:
    continue
  if i >= m:
    print(i)