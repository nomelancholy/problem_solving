pn1 = input()
pn2 = input()

pb_str = ''

for i in range(8):
  pb_str += pn1[i]
  pb_str += pn2[i]

while len(pb_str) > 2:
  new_str = ''
  
  for i in range(len(pb_str) - 1):
    new_str += str(int(pb_str[i]) + int(pb_str[i + 1]))[-1]

  pb_str = new_str

print(pb_str)