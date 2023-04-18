dwarfs = []

for _ in range(9):
  dwarfs.append(int(input()))

diff = sum(dwarfs) - 100

for i in range(9):
  for j in range(i + 1, 9):
    if dwarfs[i] + dwarfs[j] == diff:
      a = dwarfs[i]
      b = dwarfs[j]
      dwarfs.remove(a)
      dwarfs.remove(b)
      dwarfs.sort()
      break
  if len(dwarfs) == 7:
    break

for dwarf in dwarfs:
  print(dwarf)