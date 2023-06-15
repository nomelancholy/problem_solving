x = int(input())

def make_stick_half(stick, target, count):
  if stick == target:
    return count
  elif stick > target:
    return make_stick_half(stick // 2, target, count)
  else:
    return make_stick_half(stick // 2, target-stick, count + 1)

answer = make_stick_half(64, x, 1)

print(answer)