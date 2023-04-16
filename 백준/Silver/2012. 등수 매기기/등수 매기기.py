n = int(input())
ranks = []

answer = 0

for _ in range(n):
    ranks.append(int(input()))

ranks.sort()

for i, rank in enumerate(ranks):

    answer += abs((i+1) - rank)

print(answer)
