from collections import defaultdict

n = input()

word_dict = defaultdict(int)

for c in n:
  word_dict[c.upper()] += 1

max_value_key = ''

for key, value in word_dict.items():
  if value == max(word_dict.values()):
    if max_value_key == '':
      max_value_key = key
    else:
      max_value_key = '?'
      break

print(max_value_key)