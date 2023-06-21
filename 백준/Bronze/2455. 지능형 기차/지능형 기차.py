total = 0

moment = []

for _ in range(4):
    o, i = map(int, input().split())
    total -= o
    total += i
    moment.append(total)
    
print(max(moment))