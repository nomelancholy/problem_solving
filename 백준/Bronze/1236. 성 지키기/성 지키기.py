from collections import defaultdict

n, m = map(int, input().split())

answer = 0

x_dict = defaultdict(int)
y_dict = defaultdict(int)

for i in range(n):
    x_dict[i] = 0

for i in range(m):
    y_dict[i] = 0

for x in range(n):
    for y, c in enumerate(list(input())):
        if c == 'X':
            x_dict[x] += 1
            y_dict[y] += 1



x_count = len([x for x in x_dict.items() if x[1] == 0])
y_count = len([y for y in y_dict.items() if y[1] == 0])

answer = max(x_count, y_count)
print(answer)