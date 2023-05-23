def solution(arr, queries):
    
    for i in range(len(queries)):
        s, e, k = queries[i]
        
        for index in range(s, e + 1):
            if index % k == 0:
                arr[index] += 1
    
    return arr