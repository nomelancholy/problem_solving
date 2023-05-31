x, y, w, h = map(int, input().split())

answer = 1001

answer = min(answer, x - 0)
answer = min(answer, w - x)
answer = min(answer, y - 0)
answer = min(answer, h - y)

print(answer)