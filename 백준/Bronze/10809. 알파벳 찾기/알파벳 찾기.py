count_dict = {}

for ascii in range(97, 123):
  count_dict[chr(ascii)] = -1

string = input()

for i, c in enumerate(string):
  if count_dict[c] == -1:
    count_dict[c] = i

for c in count_dict.values():
  print(c, end=' ')