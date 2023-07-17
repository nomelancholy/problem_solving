n = int(input())

paper = []

for _ in range(n):
  paper.append(list(map(int, input().split())))

def is_all_clear(arr, standard):
  flag = True
  
  for i in range(len(arr)):
    for j in range(len(arr[i])):
      if arr[i][j] != standard:
        flag = False
        break

  return flag 

def recursion(arr):
  global white
  global blue

  # 하얀색 검사
  if is_all_clear(arr, 0):
    white += 1
    return
  # 파란색 검사
  elif is_all_clear(arr, 1):
    blue += 1
    return
  else:
    bp = len(arr) // 2
    lt = []
    rt = []
    lb = []
    rb = []
    
    for i in range(bp):
      line = []
      for j in range(bp):
        line.append(arr[i][j])
      lt.append(line)

    for i in range(bp):
      line = []
      for j in range(bp, bp + bp):
        line.append(arr[i][j])
      rt.append(line)

    for i in range(bp, bp + bp):
      line = []
      for j in range(bp):
        line.append(arr[i][j])
      lb.append(line)

    for i in range(bp, bp + bp):
      line = []
      for j in range(bp, bp + bp):
        line.append(arr[i][j])
      rb.append(line)

    recursion(lt)
    recursion(rt)
    recursion(lb)
    recursion(rb)

white = 0
blue = 0

recursion(paper)

print(white)
print(blue)