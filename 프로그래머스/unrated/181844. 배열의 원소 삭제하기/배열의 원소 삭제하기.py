def solution(arr, delete_list):
    answer = []
    
    for number in arr:
        if not number in delete_list:
            answer.append(number)
            
    return answer