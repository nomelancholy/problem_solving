from collections import defaultdict

n = input()

number_dict = defaultdict(int)

for c in n:
  number_dict[int(c)] += 1

else_number = 0

if 6 in number_dict:
  else_number += number_dict[6]
  del number_dict[6]
if 9 in number_dict:
  else_number += number_dict[9]
  del number_dict[9]

div, mod = divmod(else_number, 2)

if mod == 1:
  else_number = div + 1
else:
  else_number = div 

max_number = 0

if number_dict:
  max_number = max(number_dict.values())
  
answer = max(max_number, else_number)

print(answer)