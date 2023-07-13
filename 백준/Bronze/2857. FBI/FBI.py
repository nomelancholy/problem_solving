flag = False

for i in range(5):
  s = input()

  if 'FBI' in s:
    flag = True
    print(i + 1)

if not flag:
  print('HE GOT AWAY!')