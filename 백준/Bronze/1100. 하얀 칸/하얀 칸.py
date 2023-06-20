board = []

for _ in range(8):
  board.append(list(input()))

answer = 0

for i in range(8):
  white_zone = [0, 2, 4, 6]
  if i % 2 == 0:
    white_zone = [0, 2, 4, 6]
  else:
    white_zone = [1, 3, 5, 7]
  for j in range(8):
    if j in white_zone:
      if board[i][j] == 'F':
        answer += 1

print(answer)