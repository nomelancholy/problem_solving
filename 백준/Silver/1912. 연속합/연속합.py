n = int(input())
numbers = list(map(int, input().split()))

# i번째 값이 i-1보다 작을 경우는 어차피 최대 값이 될 수 없다. 
# 그 뒤에 아무리 큰 숫자가 나와도 i + 1부터 센 게 더 클테니까
for i in range(1, n):
    numbers[i] = max(numbers[i] , numbers[i] + numbers[i - 1])

print(max(numbers))