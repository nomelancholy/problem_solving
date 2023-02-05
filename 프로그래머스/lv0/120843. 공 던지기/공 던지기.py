def solution(numbers, k):
    answer = 0
    
    friends = numbers * k
    
    for i in range(0, k * 2, 2):
        answer = friends[i]
        
    return answer