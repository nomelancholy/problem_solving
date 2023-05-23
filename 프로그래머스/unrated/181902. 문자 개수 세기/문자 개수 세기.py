from collections import defaultdict

def solution(my_string):
    
    number_dict = defaultdict(int)
    
    upper = [chr(i) for i in range(65, 91)]
    lower = [chr(i) for i in range(97, 123)]
    
    for alphabet in upper:
        number_dict[alphabet] = 0
        
    for alphabet in lower:
        number_dict[alphabet] = 0
    
    for c in my_string:
        number_dict[c] += 1
    
    answer = list(number_dict.values())
    
    return answer