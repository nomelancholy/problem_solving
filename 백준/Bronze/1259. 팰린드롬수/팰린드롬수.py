while True:
  c = input()
  if c == '0':
    break
    
  reverse_c = c[::-1]

  is_same = True
  
  for i in range(len(c)):
    if c[i] != reverse_c[i]:
      is_same = False
      break
      
  if is_same:
    print('yes')
  else:
    print('no')
  