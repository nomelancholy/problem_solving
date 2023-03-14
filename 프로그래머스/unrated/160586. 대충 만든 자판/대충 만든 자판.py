def solution(keymap, targets):
    answer = []
    
    for target in targets:
        
        count = 0
        
        for c in target:
            min_index = 101
             
            for key in keymap:
                index = key.find(c)
                if index != -1:
                    min_index = min(min_index, index + 1)
            
            if min_index == 101:
                count = -1
                break
            else:
                count += min_index
        
        answer.append(count)
            
    return answer