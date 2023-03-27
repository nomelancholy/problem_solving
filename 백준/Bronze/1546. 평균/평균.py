n = int(input())

scores = list(map(int, input().split()))
scores.sort()

max_score = scores[-1]
scores = scores[:-1]

new_scores = [score / max_score * 100 for score in scores]
new_scores.append(100)

print(sum(new_scores) / len(new_scores))