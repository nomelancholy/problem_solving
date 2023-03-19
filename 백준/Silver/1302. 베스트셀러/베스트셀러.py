from collections import defaultdict

n = int(input())

book_score = defaultdict(int)

for _ in range(n):
    title = input()
    book_score[title] += 1

answer, count = sorted(book_score.items(), key=lambda x: (-x[1], x[0]))[0]
print(answer)