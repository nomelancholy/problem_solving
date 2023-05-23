def solution(arr):
    answer = [[]]
    
    if len(arr) == len(arr[0]):
        answer = arr
    else:
        if len(arr) > len(arr[0]):
            for inside_arr in arr:
                for _ in range(len(arr) - len(inside_arr)):
                    inside_arr.append(0)
            answer = arr
        elif len(arr) < len(arr[0]):
            answer = arr
            for _ in range(len(arr[0]) - len(arr)):
                answer.append([0] * len(arr[0]))
            
    return answer