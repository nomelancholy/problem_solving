n = int(input())

seats = input()
seats = seats.replace('LL', 'C')

if 'C' in seats:
  print(len(seats) + 1)
else:
  print(n)