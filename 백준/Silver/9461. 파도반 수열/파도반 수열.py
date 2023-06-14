t = int(input())

numbers = []

fibo = []

for _ in range(t):
  numbers.append(int(input()))

k = max(numbers)

fibo.append(1)
fibo.append(1)
fibo.append(1)

if k < 3:
  print(1)
else:
  for _ in range(3, k):
    fibo.append(fibo[-3] + fibo[-2])
  
  for number in numbers:
    print(fibo[number-1])