n = int(input())

constructors = []

for i in range(1, n):
  digits = [int(c) for c in str(i)]
  result = i + sum(digits)

  if n == result:
    constructors.append(i)

if constructors:
  print(min(constructors))
else:
  print(0)