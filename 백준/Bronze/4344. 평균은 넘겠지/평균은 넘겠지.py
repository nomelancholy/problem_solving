c = int(input())

for _ in range(c):
  info = list(map(int, input().split()))
  all_student_count = info[0]
  scores = info[1:]

  average = sum(scores) / all_student_count

  high_rank_student_cnt = 0

  for score in scores:
    if score > average:
      high_rank_student_cnt += 1


  ratio = high_rank_student_cnt / all_student_count * 100

  print(format(round(ratio, 3), '.3f')+'%')
  