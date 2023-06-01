s = input()

word_set = set()
slice_range = 1

while slice_range <= len(s):
  for i in range(len(s) - slice_range + 1):
    word_set.add(s[i:i + slice_range])
  slice_range += 1

print(len(word_set))