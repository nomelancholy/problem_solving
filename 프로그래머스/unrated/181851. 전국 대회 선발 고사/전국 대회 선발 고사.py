def solution(rank, attendance):
    
    answer = 0
    
    targets = []
    
    for index, flag in enumerate(attendance):
        if flag:
            targets.append((rank[index] , index))

    targets.sort(key = lambda x:x[0])
    
    targets = targets[:3]
    a, b, c = targets    

    answer = 10000 * a[1] + 100 * b[1] + c[1]
    
    return answer