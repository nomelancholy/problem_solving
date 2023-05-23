def solution(picture, k):
    answer = []
    
    for string in picture:
        new_string = ''
        
        for c in string:
            new_string += (c * k)
            
        for _ in range(k):
            answer.append(new_string)
    
    return answer