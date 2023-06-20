n = input()
f = int(input())

start = int(n[:-2] + '00')
end = int(n[:-2] + '99')

target_number = 0

for i in range(start, end + 1):
  if i % f == 0:
    target_number = i
    break
    
print(str(target_number)[-2:])