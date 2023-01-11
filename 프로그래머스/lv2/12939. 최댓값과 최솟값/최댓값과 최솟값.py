def solution(s):
    arr = s.split()
    arr = list(map(int, arr))
    answer = '{} {}'.format(min(arr), max(arr))
    return answer