n = int(input())
car_numbers = list(map(int, input().split()))

answer = 0

for car_number in car_numbers:
  if car_number == n:
    answer += 1

print(answer)