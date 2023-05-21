def solution(n):
    answer = []
    
    for i in range(n):
        i_arr = []
        for j in range(n):
            if i == j:
                i_arr.append(1)
            else:
                i_arr.append(0)
        answer.append(i_arr)
            
    return answer