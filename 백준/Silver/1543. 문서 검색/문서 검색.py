document = input()
target = input()
answer = 0

while len(document) >= len(target):
    if document[:len(target)] == target:
        answer += 1
        document = document[len(target):]
    else:
        document = document[1:]

print(answer)