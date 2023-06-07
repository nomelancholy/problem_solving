n = int(input())

if n == 1:
  print()
else:
  prime_numbers = []
  while n > 1:
    for i in range(2, n + 1):
      if n % i == 0:
        prime_numbers.append(i)
        n //= i
        break
  
  for prime_number in prime_numbers:
    print(prime_number)