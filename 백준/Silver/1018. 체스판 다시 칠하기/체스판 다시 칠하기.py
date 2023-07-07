n, m = map(int, input().split())

board = []

for _ in range(n):
  row = list(input())
  board.append(row)

answer = 32

def color_change(copy_board):
  b_count = 0
  w_count = 0
  
  right = []
  for r in range(8):
    if r % 2 == 0:
      right = ['B','W','B','W','B','W','B','W']
    else:
      right = ['W','B','W','B','W','B','W', 'B']
    for c in range(8):
      if copy_board[r][c] != right[c]:
        b_count += 1

  for r in range(8):
    if r % 2 == 0:
      right = ['W','B','W','B','W','B','W', 'B']
    else:
      right = ['B','W','B','W','B','W','B','W']
    for c in range(8):
      if copy_board[r][c] != right[c]:
        w_count += 1
        
  return min(b_count, w_count)
    
for r in range(0, len(board) - 7):
  for c in range(0, len(board[0]) - 7):
    section = [arr[c:c + 8]for arr in board[r:r + 8]]
    change_count = color_change(section)
    answer = min(answer, change_count)

print(answer)