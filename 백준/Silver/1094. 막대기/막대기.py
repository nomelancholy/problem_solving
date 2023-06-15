x = int(input())

stick = 64
answer = 1

while stick > x:
  stick = stick // 2

def make_stick_half(stick, target, count):
  if stick == target:
    return count
  elif stick > target:
    return make_stick_half(stick // 2, target, count )
  else:
    return make_stick_half(stick // 2, target-stick, count + 1)

if stick == x:
  print(answer)
else:
  target = x - stick
  result = make_stick_half(stick // 2, target, 1)

  answer += result
  print(answer)