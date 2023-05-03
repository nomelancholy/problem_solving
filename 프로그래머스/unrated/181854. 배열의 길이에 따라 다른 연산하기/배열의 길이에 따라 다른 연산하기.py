def solution(arr, n):
    if len(arr) % 2 == 1:
        answer = [number + n if i % 2 == 0  else number for i, number in enumerate(arr)]
    else:
        answer = [number + n if i % 2 == 1  else number for i, number in enumerate(arr)]
    return answer