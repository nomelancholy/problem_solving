croatia_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()

for alpha in croatia_alphabet:
  word = word.replace(alpha, '!')

print(len(word))