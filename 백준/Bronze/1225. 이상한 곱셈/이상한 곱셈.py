a, b = input().split()

a_list = list(map(int, list(a)))
b_list = list(map(int, list(b)))

answer = 0

for a_number in a_list:
  for b_number in b_list:
    answer += a_number * b_number

print(answer)