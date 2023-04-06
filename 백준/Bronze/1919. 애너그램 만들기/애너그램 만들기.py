answer = 0

str1 = list(input())
str2 = list(input())

str1_copy = str1[::]
str2_copy = str2[::]

for c in str1:
    if c in str2_copy:
        str2_copy.remove(c)
    else:
        answer += 1

for c in str2:
    if c in str1_copy:
        str1_copy.remove(c)
    else:
        answer += 1

print(answer)