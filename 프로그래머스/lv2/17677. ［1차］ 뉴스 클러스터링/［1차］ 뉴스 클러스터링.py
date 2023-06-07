import math

def solution(str1, str2):
    CONSTANT_NUMBER = 65536
    
    answer = 0
    
    str1_list = []
    str2_list = []
    
    for i in range(len(str1) - 1):
        if str1[i : i + 2].isalpha():
            str1_list.append(str1[i : i + 2].lower())

    for i in range(len(str2) - 1):
        if str2[i : i + 2].isalpha():
            str2_list.append(str2[i : i + 2].lower())       

    if not str1_list and not str2_list:
        return CONSTANT_NUMBER
            
    intersection = []
    union = []
    
    # 교집합 구하기
    for str1_chunk in set(str1_list):
        if str1_chunk not in str2_list:
            continue
        count = min(str1_list.count(str1_chunk), str2_list.count(str1_chunk))
        
        for _ in range(count):
            intersection.append(str1_chunk)
        
    union = str1_list + str2_list
    
    for string in intersection:
        union.remove(string)
    
    answer = 0
    answer = math.trunc(len(intersection) / len(union) * CONSTANT_NUMBER)
        
    return answer