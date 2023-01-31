

def solution(array, n):
    answer = 0
    
    check_list = [0, 100]
    
    array.sort()
    
    for number in array: 
        key = check_list[0]
        difference = check_list[1]
        if number < n:
            diff = n -number
            if diff < difference:
                check_list = [number, diff]
        elif number > n:
            diff = number - n
            if diff < difference:
                check_list = [number, diff]
        else:
            return number
            
    answer = check_list[0]
            
    return answer