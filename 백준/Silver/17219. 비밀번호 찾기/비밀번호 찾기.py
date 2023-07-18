from collections import defaultdict

n, m = map(int, input().split())

site_dict = defaultdict(str)

for _ in range(n):
  site, pw = input().split()
  site_dict[site] = pw

for _ in range(m):
  site = input()
  print(site_dict[site])