def solution(arr):
    
    answer = arr
    
    two_squares = [2 ** i for i in range(0, 11)]
    
    if len(arr) not in two_squares:
        for number in two_squares:
            if len(arr) < number:
                for _ in range(number - len(arr)):
                    answer.append(0)
                break
        
    return answer