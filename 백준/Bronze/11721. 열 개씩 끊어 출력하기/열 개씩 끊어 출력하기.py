n = input()

if len(n) <= 10 :
  print(n)
else:
  start = 0
  end = 10

  while end < len(n):
    print(n[start:end])

    start = end
    end += 10

  end = len(n) + 1
  print(n[start:end])