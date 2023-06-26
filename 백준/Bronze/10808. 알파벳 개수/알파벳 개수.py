count_list = [0 for _ in range(26)]

s = input()

for c in s:
  count_list[ord(c) - 97] += 1

for c in count_list:
  print(c, end=" ")