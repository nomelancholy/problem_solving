from collections import defaultdict

fn_dict = defaultdict(int)

n = int(input())

for _ in range(n):
   fn_dict[input()[0]] += 1

candidates = [k for k, v in fn_dict.items() if v >= 5]
candidates.sort()

if candidates:
  print(''.join(candidates))
else:
  print("PREDAJA")