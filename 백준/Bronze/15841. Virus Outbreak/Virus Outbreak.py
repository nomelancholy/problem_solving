x_list = []

while True:
  n = int(input())
  if n == -1:
    break

  x_list.append(n)

y_list = [0, 1, 1]

end = max(x_list)

if end > 2:
  for _ in range(end):
    y_list.append(y_list[-2] + y_list[-1])
  
for x in x_list:
  print(f'Hour {x}: {y_list[x]} cow(s) affected')