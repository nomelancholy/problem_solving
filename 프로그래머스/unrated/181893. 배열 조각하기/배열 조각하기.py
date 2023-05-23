def solution(arr, query):
    
    for i, index in enumerate(query):
        if i % 2 == 0:
            arr = arr[:index + 1]
        else:
            arr = arr[index:]
    
    return arr