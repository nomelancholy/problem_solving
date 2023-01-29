def solution(array):
    answer = []
    
    max_number = max(array)
    
    answer = [max_number, array.index(max_number)]
    
    return answer