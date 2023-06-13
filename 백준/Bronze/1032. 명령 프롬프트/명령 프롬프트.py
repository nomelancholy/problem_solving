n = int(input())

file_names = []

for _ in range(n):
  file_names.append(input())

answer = ''

for i in range(len(file_names[0])):
  character = ''
  for file_name in file_names:
    if character == '' or character == file_name[i]:
      character = file_name[i]
    else:
      character = '?'
      break
  answer += character

print(answer)