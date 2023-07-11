import sys

input = sys.stdin.readline

n, m = map(int, input().split())

numbers = list(map(int, input().split()))

acc = [0]

for n in numbers:
  acc.append(acc[-1] + n)

for _ in range(m):
  start, end = map(int, input().split())
  print(acc[end] - acc[start - 1])