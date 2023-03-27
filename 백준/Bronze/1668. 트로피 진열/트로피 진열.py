n = int(input())
trophies = []
for _ in range(n):
    t = int(input())
    trophies.append(t)

left = 1
right = 1

left_seen = trophies[0]
right_seen = trophies[n - 1]

for i in range(1, len(trophies)):
    if trophies[i] > left_seen:
        left += 1
        left_seen = trophies[i]

for i in range(len(trophies) - 2, -1, -1):
    if trophies[i] > right_seen:
        right += 1
        right_seen = trophies[i]
    
print(left)
print(right)