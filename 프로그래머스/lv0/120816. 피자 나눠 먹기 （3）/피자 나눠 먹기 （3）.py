def solution(slice, n):
    v, r =divmod(n, slice)
    answer = v
    if r != 0:
        answer += 1
    return answer