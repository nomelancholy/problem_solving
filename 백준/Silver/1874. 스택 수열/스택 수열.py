n = int(input())

count = 1
stack = []
commands = []

for _ in range(n):
    target = int(input())
    while count <= target:
        stack.append(count)
        count += 1
        commands.append('+')
    if stack[-1] == target:
        stack.pop()
        commands.append('-')
    else:
        commands.clear()
        break

if commands:
    for command in commands:
        print(command)
else:
    print('NO')