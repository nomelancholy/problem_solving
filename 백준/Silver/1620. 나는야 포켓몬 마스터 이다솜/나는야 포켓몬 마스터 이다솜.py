from collections import defaultdict

n, m = map(int, input().split())

pokemon_dict = {}
pokemon_num_dict = {}

for i in range(1, n + 1):
  name = input()
  pokemon_dict[name] = i
  pokemon_num_dict[i] = name

for _ in range(m):
  q = input()

  if q.isdigit():
    print(pokemon_num_dict[int(q)])
  else:
    print(pokemon_dict[q])