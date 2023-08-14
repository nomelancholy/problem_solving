from collections import deque

n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
m = int(input())
c = list(map(int, input().split()))

q = deque()

for i, is_q in enumerate(a):
  if is_q == 0:
    q.appendleft(b[i])

for i in range(m):
  q.append(c[i])
  print(q.popleft(), end=' ')