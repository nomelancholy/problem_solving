while True:
  s = input()
  if s == '.':
    break

  result = True
  stack = []
  
  for c in s:
    if c == '(' or c =='[':
      stack.append(c)
    elif c == ')' or c == ']':
      if not stack:
        result = False
        break
      
      if c == ')':
        if stack[-1] == '(':
          stack.pop()
        else:
          result = False
          break
      elif c == ']':
        if stack[-1] == '[':
          stack.pop()
        else:
          result = False
          break        
    
  if stack:
    result = False

  if result:
    print('yes')
  else:
    print('no')