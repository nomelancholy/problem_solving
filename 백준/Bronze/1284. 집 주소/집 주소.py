while True:
  n = input()

  answer = 1
  
  if n == '0':
    break

  for c in n:
    if c == '0':
      answer += 4
    elif c == '1':
      answer += 2
    else:
      answer += 3
    answer += 1

  print(answer)