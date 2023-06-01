from collections import defaultdict

count_dict = defaultdict(int)

n = int(input())
numbers = list(map(int, input().split()))

for number in numbers:
  count_dict[number] += 1

m = int(input())

check_list = list(map(int, input().split()))

for number in check_list:
  if count_dict.get(number):
    print(count_dict[number], end=' ')
  else:
    print(0, end=' ')