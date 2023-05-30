a = int(input())
b = int(input())
c = int(input())

total = a * b * c

number_dict = { i : 0 for i in range(10)}

for c in str(total):
  number_dict[int(c)] += 1

for count in number_dict.values():
  print(count)