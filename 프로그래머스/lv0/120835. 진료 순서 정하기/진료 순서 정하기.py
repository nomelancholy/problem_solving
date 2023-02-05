def solution(emergency):
    answer = [0] * len(emergency)
    
    tuple_list =[]
    
    for index, rate in enumerate(emergency):
        tuple_list.append((rate, index))
    
    tuple_list.sort(key=lambda x:x[0], reverse=True)
    
    for index, t in enumerate(tuple_list):
        answer[t[1]] = index + 1
    
    return answer