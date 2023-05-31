m = int(input())
n = int(input())

prime_numbers = []

for i in range(m, n + 1):
  if i == 1:
    continue
  is_prime = True
  for j in range(2, i // 2 + 1):
    if i % j == 0:
      is_prime = False
      break
  
  if is_prime:
    prime_numbers.append(i)

if prime_numbers:
  print(sum(prime_numbers))
  print(min(prime_numbers))
else:
  print(-1)