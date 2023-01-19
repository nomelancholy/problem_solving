def solution(priorities, location):
    answer = 0
    
    arr = [(priority, index) for index, priority in enumerate(priorities)]
    
    while True:
        p, i = arr.pop(0)
        if list(filter(lambda x: x[0] > p, arr)):
            arr.append((p, i))
        else:
            answer += 1
            if i == location:
                break
        
    return answer