black_board = []

longest_word_count = 0

for _ in range(5):
  words = list(input())
  longest_word_count = max(longest_word_count, len(words))
  black_board.append(words)

answer = ''

for c in range(longest_word_count):
  for r in range(len(black_board)):
    if c < len(black_board[r]):
      answer += black_board[r][c]
      
print(answer)
