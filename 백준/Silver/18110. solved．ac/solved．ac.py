import heapq

def get_round(p):
  if p - int(p) >= 0.5:
    return int(p)  + 1
  else:
    return int(p)

n = int(input())
opinions = []

for _ in range(n):
  opinions.append(int(input()))

heapq.heapify(opinions)
cut_line = get_round(n * 0.15)

for _ in range(cut_line):
  heapq.heappop(opinions)

max_heap = []
# 최대 힙으로 변경
for opinion in opinions:
  heapq.heappush(max_heap, -opinion)

for _ in range(cut_line):
  heapq.heappop(max_heap)

validate_values = []

for v in max_heap:
  validate_values.append(-v)

if sum(validate_values) == 0:
  print(0)
else:
  print(get_round(sum(validate_values) / len(validate_values)))