n, b = map(int, input().split())

answer = ''

while n != 0:
  div, mod = divmod(n, b)
  n = div
  
  if mod >= 10:
    answer += chr(mod + 55)
  else:
    answer += str(mod)

print(answer[::-1])