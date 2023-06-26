l, p = map(int, input().split())

right = l * p

news_count = list(map(int, input().split()))

for count in news_count:
  print(count - right, end=' ')