n, m = map(int, input().split())

s = []
answer = 0

for _ in range(n):
  s.append(input())

s_dict = {c : True for c in s}

for _ in range(m):
  string = input()
  if s_dict.get(string):
    answer += 1

print(answer)