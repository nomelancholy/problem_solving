def solution(s):
    
    count = 0
    zero_count = 0
    
    # s가 1이 될 때 까지 반복
    while s != '1':
        count += 1
        
        before = len(s)
        after = len(s.replace('0', ''))
        
        zero_count += (before - after)
                
        s = format(after, 'b')
    
    answer = [count, zero_count]
    
    return answer