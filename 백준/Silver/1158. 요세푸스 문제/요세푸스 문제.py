from collections import deque

n, k = map(int, input().split(' '))

count = 0
numbers = deque([i + 1 for i in range(n)])

answer = []

while numbers:
    count += 1
    target = numbers.popleft()
    if count % k == 0:
        answer.append(target)
    else:
        numbers.append(target)

print('<', end="")
for i, n in enumerate(answer):

    if i < len(answer) - 1:
        print(n, end=", ")
    else:
        print(n, end="")
print('>')
