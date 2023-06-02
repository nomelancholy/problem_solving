from math import sqrt

n = int(input())

answer = 0

for _ in range(n):
  number = int(input())

  if number == 1 or number == 0:
    print(2)
  else:
    while True:
  
      did_found = True
      
      for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
          did_found = False
          break
  
      if did_found:
        answer = number
        break
        
      number += 1
    print(answer)