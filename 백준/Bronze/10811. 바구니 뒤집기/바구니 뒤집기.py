n, m = map(int, input().split())

numbers = [i for i in range(1, n + 1)]

for _ in range(m):
  start, end = map(int, input().split()) 
  
  start -= 1
  end -= 1

  numbers = numbers[:start] + list(reversed(numbers[start:end + 1])) + numbers[end +1 :]


for number in numbers:
  print(number, end= ' ')