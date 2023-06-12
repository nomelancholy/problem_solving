from collections import deque

n, k = map(int, input().split())

q = deque([i for i in range(1, n + 1)])

turn = 0

answer = []

while q:
  turn += 1
  now = q.popleft()
  if turn % k == 0:
    answer.append(str(now))
  else:
    q.append(now)

print('<', end='')
numbers_str = ', '.join(answer)
print(numbers_str, end='')
print('>')