from collections import deque

left_deque = deque(list(input()))
right_deque = deque()

n = int(input())

for _ in range(n):
    command = input()

    if command[0] == 'L':
        if left_deque:
            c = left_deque.pop()
            right_deque.appendleft(c)
    elif command[0] == 'D':
        if right_deque:
            c = right_deque.popleft()
            left_deque.append(c)
    elif command[0] == 'B':
        if left_deque:
            left_deque.pop()
    elif command[0] == 'P':
        c = command.split()[1]
        left_deque.append(c)

left = ''.join(left_deque)
right = ''.join(right_deque)

print(left + right)
