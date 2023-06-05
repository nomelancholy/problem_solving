a, b = map(int, input().split())

a_list = [a]
b_list = [b]

if '5' in str(a):
  a_list.append(int(str(a).replace('5','6')))
  
if '6' in str(a):
  a_list.append(int(str(a).replace('6', '5')))
  
if '5' in str(b):
  b_list.append(int(str(b).replace('5', '6')))  
  
if '6' in str(b):
  b_list.append(int(str(b).replace('6', '5')))  

print(min(a_list) + min(b_list), end=' ')
print(max(a_list) + max(b_list))