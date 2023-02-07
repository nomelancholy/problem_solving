def solution(numlist, n):
    answer = []
    
    diff_list = []
    
    for num in numlist:
        diff = 0
        if num >= n:
            diff = num - n
        else:
            diff = n - num
        diff_list.append((num, diff))
    
    diff_list.sort(key=lambda x : (x[1],  -x[0]))
            
    for num, diff in diff_list:
        answer.append(num)
    
    return answer