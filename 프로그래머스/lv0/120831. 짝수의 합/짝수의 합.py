def solution(n):
    evens = [i for i in range(n + 1) if i % 2 == 0]
    answer = sum(evens)
    return answer