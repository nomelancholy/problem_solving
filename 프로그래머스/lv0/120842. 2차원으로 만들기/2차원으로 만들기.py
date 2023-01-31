def solution(num_list, n):
    answer = []
    index = 0
    for i in range(n, len(num_list) + 1, n) :
        answer.append(num_list[index:i])
        index = i
    
    return answer