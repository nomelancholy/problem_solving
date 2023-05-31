t = int(input())

coin_kinds = [25, 10, 5, 1]

for _ in range(t):
  answer = []
  change = int(input())
  for coin in coin_kinds:  
    
    div, mod = divmod(change, coin)
    answer.append(div)
    change = mod
    
  for n in answer:
    print(n, end=' ')
  print()