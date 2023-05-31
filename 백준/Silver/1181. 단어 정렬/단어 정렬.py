n = int(input())

word_set = set()

for _ in range(n):
  word_set.add(input())

sorted_list = sorted(list(word_set), key=lambda x: (len(x), x))

for word in sorted_list:
  print(word)