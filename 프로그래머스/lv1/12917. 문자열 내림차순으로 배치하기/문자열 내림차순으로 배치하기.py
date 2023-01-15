def solution(s):
    arr = [c for c in s]
    arr.sort(reverse=True)
    answer = ''.join(arr)
    return answer