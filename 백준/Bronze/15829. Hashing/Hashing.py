l = int(input())
s = input()

sum = 0
r = 31
m = 1234567891

for i, c in enumerate(s):
  sum += ((ord(c) - 96) * (r ** i)) % m

print(sum % m)