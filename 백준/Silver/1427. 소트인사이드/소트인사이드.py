input_list = list(map(int, list(input())))
input_list.sort(reverse=True)

answer = ''

for n in input_list:
    answer += str(n)

print(answer)