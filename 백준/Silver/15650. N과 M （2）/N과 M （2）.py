from itertools import combinations

n, m = map(int, input().split())

arr = [i for i in range(1, n + 1)]

for sets in list(combinations(arr, m)):
  for ele in sets:
    print(ele, end=' ')
  print("")