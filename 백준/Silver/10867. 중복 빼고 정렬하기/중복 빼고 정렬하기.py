n = int(input())

numbers = sorted(set(map(int, input().split())))

for number in numbers:
  print(number, end=' ')