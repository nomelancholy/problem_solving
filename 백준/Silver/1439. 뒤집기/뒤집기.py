numbers = list(input())

compressed = ''

for number in numbers:
    if len(compressed) > 0:
        if compressed[-1] != number:
            compressed += number
    else:
        compressed += number

answer = min(compressed.count('0'), compressed.count('1'))            

print(answer)