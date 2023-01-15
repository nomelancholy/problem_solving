def solution(a, b):
    numbers = [x * y for x, y in zip(a, b)]
    answer = sum(numbers)
    return answer