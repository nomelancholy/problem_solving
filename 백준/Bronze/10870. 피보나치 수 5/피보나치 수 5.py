n = int(input())
numbers = [0, 1]

if n == 0:
  print(0)
elif n == 1:
  print(1)
else:  
  for _ in range(2, n + 1):
    numbers.append(numbers[-2] + numbers[-1])
  
  print(numbers[-1])