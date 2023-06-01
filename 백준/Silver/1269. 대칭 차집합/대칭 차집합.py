a_cnt, b_cnt = map(int, input().split())

a = set(map(int, input().split()))
b = set(map(int, input().split()))

answer = len(a - b)
answer += len(b - a)

print(answer)