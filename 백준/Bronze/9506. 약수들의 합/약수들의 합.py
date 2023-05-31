while True:
  n = int(input())

  if n == -1:
    break

  factors = []
  
  for i in range(1, n // 2 + 1):
    if n % i == 0:
      factors.append(i)

  if n == sum(factors):
    print(n, end=' = ')
    for i, factor in enumerate(factors):
      if i < len(factors) - 1:
        print(factor, end=' + ')
      else:
        print(factor)
  else:
    print(f'{n} is NOT perfect.')   