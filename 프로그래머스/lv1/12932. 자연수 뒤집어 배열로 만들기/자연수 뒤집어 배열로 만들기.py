def solution(n):
    answer = [i for i in str(n)]
    answer.reverse()
    answer = list(map(int, answer))
    return answer