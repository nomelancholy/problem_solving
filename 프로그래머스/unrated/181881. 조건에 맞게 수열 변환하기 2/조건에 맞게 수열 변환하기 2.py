def solution(arr):
    answer = 0
    
    temp_arr = [arr]
    
    while True:
        new_arr = []
        for ele in temp_arr[-1]:
            if ele >= 50:
                if ele % 2 == 0:
                    ele = ele // 2
            else:
                if ele % 2 == 1:
                    ele = ele * 2 + 1
            new_arr.append(ele)
        temp_arr.append(new_arr)
        if temp_arr[-2] == temp_arr[-1]:
            break
    
    answer = len(temp_arr) - 2
    
    return answer