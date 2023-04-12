from collections import deque

repeat = int(input())
answer = []

for _ in range(repeat): 
    _, m = map(int, input().split())
    priority = list(map(int, input().split()))

    q = deque()

    for index, p in enumerate(priority):
        q.append((index, p))

    count = 0

    while q:

        top = q.popleft()
        isCanPrint = True

        if q:
            for item, p in q:
                if p > top[1]:
                    isCanPrint = False
                    break

        if isCanPrint:
            count += 1 
            if top[0] == m:
                answer.append(count)
                break
        else:
            q.append(top)

for result in answer:
    print(result)