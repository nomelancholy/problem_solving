e, s, m = map(int, input().split())

count = 0

ec = 1 
sc = 1 
mc = 1

while True:
  count += 1
  if ec == e and sc == s and mc == m:
    break
  else:
    ec += 1
    if ec > 15:
      ec = 1
    sc += 1
    if sc > 28:
      sc = 1
    mc += 1
    if mc > 19:
      mc = 1

print(count)