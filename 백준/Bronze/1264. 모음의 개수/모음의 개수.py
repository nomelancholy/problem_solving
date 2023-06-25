vowels = ['a', 'e', 'i', 'o', 'u']

while True:
  s = input()

  if s == '#':
    break

  count = 0
  
  for c in s.lower():
    if c in vowels:
      count += 1

  print(count)