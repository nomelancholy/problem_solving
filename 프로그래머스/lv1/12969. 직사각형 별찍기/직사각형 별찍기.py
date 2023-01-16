a, b = map(int, input().strip().split(' '))
for i in range(b):
    n = ''
    for j in range(a):
        n += '*'
    print(n)