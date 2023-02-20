def solution(dirs):
    answer = 0
    
    tuple_set = set()
    
    now = (5, 5)
    prev = (5, 5)
    
    direction_constant = ['U', 'R', 'D', 'L']
    # 상우하좌 / URDL
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    
    for direction in dirs:
        r, c = now
        
        di = direction_constant.index(direction)
        
        nr = dr[di] + r
        nc = dc[di] + c
        
        if nr < 0 or nr > 10 or nc < 0 or nc > 10:
            continue
        
        prev = (r, c)
        now = (nr, nc)
            
        now = (nr, nc)
    
        if (now, prev) not in tuple_set:
            tuple_set.add((prev, now))
        
    answer = len(tuple_set)
    
    return answer