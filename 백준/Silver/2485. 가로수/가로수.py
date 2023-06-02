from math import gcd

n = int(input())

tree_points = []

for _ in range(n):
  tree_points.append(int(input()))

distances = []

for i in range(len(tree_points)-1, 0, -1):
  distances.append(tree_points[i] - tree_points[i-1])

common_gcd = 1

for i in range(len(distances)-1):
  if i == 0:
    common_gcd = gcd(distances[i], distances[i + 1])
  else:
    common_gcd = gcd(common_gcd, distances[i + 1])

answer = 0

for distance in distances:
  answer += distance // common_gcd - 1

print(answer)