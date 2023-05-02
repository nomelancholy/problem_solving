from math import prod

def solution(num_list):
    answer = 0
    
    all_sum = sum(num_list) 
    all_prod = prod(num_list)
    
    if all_prod < all_sum ** 2:
        answer = 1
    
    return answer