def solution(array):
    answer = 0
    
    for number in array:
        answer += str(number).count('7') 
    
    return answer