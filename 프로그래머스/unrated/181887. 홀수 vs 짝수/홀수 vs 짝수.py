def solution(num_list):
    answer = 0
    
    odd_sum = 0
    even_sum = 0
    
    for i, n in enumerate(num_list):
        if i % 2 == 0:
            odd_sum += n
        else:
            even_sum += n
            
    answer = max(odd_sum, even_sum)
    
    return answer