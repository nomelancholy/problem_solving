def solution(n):
    v,r = divmod(n, 7)
    answer = v
    if r != 0:
        answer += 1
    return answer