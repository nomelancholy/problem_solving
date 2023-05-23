def solution(arr):
    answer = []
    
    index_list = [i for i, v in enumerate(arr) if v == 2]
    
    if index_list:
        if len(index_list) == 1:
            answer.append(arr[index_list[0]])
        else:
            s = index_list[0]
            e = index_list[-1]
            answer = arr[s:e + 1]
            
    else:
        answer.append(-1)        
    
    return answer