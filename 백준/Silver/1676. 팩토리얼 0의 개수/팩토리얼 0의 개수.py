n = int(input())
factorial = 1

numbers = [i for i in range(1, n + 1)]

for number in numbers:
    factorial = number * factorial

reversed_factorial_str = str(factorial)[::-1]

answer = 0

for i, c in enumerate(reversed_factorial_str):
  if c != '0':
    answer = i 
    break

print(answer)