T = int(input())

for _ in range(T):
  temp_arr = input().split()
  R = int(temp_arr[0])
  string = temp_arr[1]

  answer = ''
    
  for c in string:
    answer += c * R

  print(answer)