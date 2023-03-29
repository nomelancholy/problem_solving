import heapq

n = int(input())

numbers = []
answer = 0

for _ in range(n):
    heapq.heappush(numbers, int(input()))
    
while len(numbers) != 1:
    first = heapq.heappop(numbers)
    second = heapq.heappop(numbers)
    
    sum_value = first + second
    
    answer += sum_value
    
    heapq.heappush(numbers, sum_value)
    
print(answer)