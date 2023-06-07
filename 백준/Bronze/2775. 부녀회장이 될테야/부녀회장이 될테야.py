t = int(input())

pairs = []

max_k = 0
max_n = 0

for _ in range(t):
  k = int(input())
  n = int(input())
  
  pairs.append((k, n))

  max_k = max(max_k, k)
  max_n = max(max_n, n)
  
first_line = [i for i in range(1, max_n + 1)]
apt = [first_line]
for i in range(1, max_k + 1):
  line = []
  for j in range(max_n):
    line.append(sum(apt[i-1][:j + 1]))
  
  apt.append(line)

for k, n in pairs:
  print(apt[k][n-1])
  